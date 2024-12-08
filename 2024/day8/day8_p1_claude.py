from typing import List, Set, Tuple
from collections import defaultdict
from math import gcd


def parse_input(grid: str) -> dict:
    """Parse the input grid and return a dictionary of frequency: list of positions."""
    frequencies = defaultdict(list)
    lines = grid.strip().split('\n')

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != '.' and char != '#':  # Ignore '#' as they're antinodes
                frequencies[char].append((x, y))

    return frequencies


def normalize_vector(dx: int, dy: int) -> Tuple[int, int]:
    """Normalize a vector by dividing by GCD."""
    if dx == 0 and dy == 0:
        return (0, 0)
    if dx == 0:
        return (0, 1 if dy > 0 else -1)
    if dy == 0:
        return (1 if dx > 0 else -1, 0)

    d = gcd(abs(dx), abs(dy))
    return (dx // d, dy // d)


def find_antinodes(positions: List[Tuple[int, int]], bounds: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Find all antinodes created by antennas of the same frequency."""
    width, height = bounds
    antinodes = set()

    for i, (x1, y1) in enumerate(positions):
        for j, (x2, y2) in enumerate(positions):
            if i >= j:  # Skip duplicate pairs
                continue

            # Calculate vector between points
            dx = x2 - x1
            dy = y2 - y1

            # Skip if points are the same
            if dx == 0 and dy == 0:
                continue

            # Get normalized direction vector
            dir_x, dir_y = normalize_vector(dx, dy)

            # Calculate total steps between points
            steps = max(abs(dx), abs(dy))

            # For each point along the line in both directions
            for step in range(-steps * 2, steps * 3):  # Check points beyond antennas
                x = x1 + dir_x * step
                y = y1 + dir_y * step

                # Skip if point is out of bounds
                if not (0 <= x < width and 0 <= y < height):
                    continue

                # Calculate distances to both antennas
                d1 = abs((x - x1) * dir_x + (y - y1) * dir_y)
                d2 = abs((x - x2) * dir_x + (y - y2) * dir_y)

                # Check if one distance is twice the other
                if d1 > 0 and d2 > 0 and (d1 == 2 * d2 or d2 == 2 * d1):
                    antinodes.add((int(x), int(y)))

    return antinodes


def solve_antenna_problem(input_grid: str) -> int:
    """Calculate total number of unique antinode locations."""
    lines = input_grid.strip().split('\n')
    width, height = len(lines[0].strip()), len(lines)

    # Get antenna positions by frequency
    frequencies = parse_input(input_grid)

    print(f"Found {len(frequencies)} different frequencies")
    print("Grid dimensions:", width, "x", height)

    # Find all antinodes
    all_antinodes = set()
    for freq, positions in frequencies.items():
        if len(positions) >= 2:
            antinodes = find_antinodes(positions, (width, height))
            print(f"Frequency '{freq}' ({len(positions)} antennas): Found {len(antinodes)} antinodes")
            all_antinodes.update(antinodes)

    return len(all_antinodes)


# Read input from file
with open('input8.txt', 'r') as file:
    input_data = file.read()

result = solve_antenna_problem(input_data)
print(f"\nFinal number of unique antinode locations: {result}")
