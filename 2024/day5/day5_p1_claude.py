from typing import List, Dict, Set, Tuple
from collections import defaultdict


def read_input_file(filename: str) -> str:
    """Read input data from file."""
    with open(filename, 'r') as f:
        return f.read()


def parse_input_data(raw_data: str) -> Tuple[Dict[int, Set[int]], List[List[int]]]:
    """Parse the raw input data into rules and updates."""
    # Split into rules and updates sections
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


def solve_puzzle(rules: Dict[int, Set[int]], updates: List[List[int]]) -> int:
    """
    Solve the puzzle using the parsed rules and updates.
    Returns the sum of middle pages from valid updates.
    """
    valid_middle_pages = []

    for update in updates:
        if is_valid_sequence(update, rules):
            middle_page = update[len(update) // 2]
            valid_middle_pages.append(middle_page)

    return sum(valid_middle_pages)


if __name__ == "__main__":
    try:
        # Read and process the data
        raw_data = read_input_file('input5.txt')
        rules, updates = parse_input_data(raw_data)

        # Solve the puzzle
        result = solve_puzzle(rules, updates)
        print(f"Sum of middle pages from valid updates: {result}")

    except FileNotFoundError:
        print("Error: Could not find input5.txt")
    except Exception as e:
        print(f"Error processing data: {e}")
