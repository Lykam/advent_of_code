from typing import List, Dict, Set, Tuple
from collections import defaultdict


def read_input_file(filename: str) -> str:
    """Read input data from file."""
    with open(filename, 'r') as f:
        return f.read()


def parse_input_data(raw_data: str) -> Tuple[Dict[int, Set[int]], List[List[int]]]:
    """Parse the raw input data into rules and updates."""
    sections = raw_data.strip().split('\n\n')
    rules_text = sections[0]
    updates_text = sections[1] if len(sections) > 1 else ""

    # Parse rules
    rules = defaultdict(set)
    for line in rules_text.split('\n'):
        if '|' in line:
            before, after = map(int, line.strip().split('|'))
            rules[before].add(after)

    # Parse updates
    updates = []
    if updates_text:
        for line in updates_text.split('\n'):
            if line.strip():
                updates.append([int(x) for x in line.strip().split(',')])

    return rules, updates


def is_valid_sequence(sequence: List[int], rules: Dict[int, Set[int]]) -> bool:
    """Check if a sequence of pages satisfies all rules."""
    positions = {page: i for i, page in enumerate(sequence)}

    for pos, page in enumerate(sequence):
        if page in rules:
            for must_come_after in rules[page]:
                if must_come_after in positions:
                    if positions[must_come_after] <= pos:
                        return False
    return True


def build_dependency_graph(rules: Dict[int, Set[int]], pages: Set[int]) -> Dict[int, Set[int]]:
    """Build a complete dependency graph for the given pages."""
    graph = defaultdict(set)
    for page in pages:
        if page in rules:
            graph[page].update(rules[page])

    # Add transitive dependencies
    changed = True
    while changed:
        changed = False
        for page in list(graph.keys()):
            deps = graph[page].copy()
            for dep in deps:
                if dep in graph:
                    new_deps = graph[dep] - graph[page]
                    if new_deps:
                        graph[page].update(new_deps)
                        changed = True

    return graph


def topological_sort(pages: List[int], rules: Dict[int, Set[int]]) -> List[int]:
    """Sort pages according to dependencies using topological sort."""
    page_set = set(pages)
    graph = build_dependency_graph(rules, page_set)

    # Calculate in-degrees
    in_degree = defaultdict(int)
    for page in pages:
        for dependent in graph.get(page, set()):
            if dependent in page_set:
                in_degree[dependent] += 1

    # Initialize result and queue
    result = []
    queue = [page for page in pages if in_degree[page] == 0]

    # Process queue
    while queue:
        page = queue.pop(0)
        result.append(page)

        for dependent in graph.get(page, set()):
            if dependent in page_set:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)

    return result


def solve_part2(rules: Dict[int, Set[int]], updates: List[List[int]]) -> int:
    """Solve part 2: Find incorrectly ordered updates, fix them, and sum their middle pages."""
    middle_pages = []

    for update in updates:
        if not is_valid_sequence(update, rules):
            reordered = topological_sort(update, rules)
            middle_page = reordered[len(reordered) // 2]
            middle_pages.append(middle_page)

    return sum(middle_pages)


if __name__ == "__main__":
    try:
        raw_data = read_input_file('input5.txt')
        rules, updates = parse_input_data(raw_data)
        result = solve_part2(rules, updates)
        print(f"Sum of middle pages from reordered incorrect updates: {result}")

    except FileNotFoundError:
        print("Error: Could not find input5.txt")
    except Exception as e:
        print(f"Error processing data: {e}")
