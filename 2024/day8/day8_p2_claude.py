from typing import List, Set, Tuple
from collections import defaultdict


def parse_input(grid: str) -> dict:
    """Parse the input grid and return a dictionary of frequency: list of positions."""
    frequencies = defaultdict(list)
    lines = grid.strip().split('\n')

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            if char != '.' and char != '#':
                frequencies[char].append((x, y))

    return frequencies


def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points are collinear using cross product."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Calculate cross product
    cross_product = (y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)
    return cross_product == 0


def find_antinodes(positions: List[Tuple[int, int]], bounds: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Find all antinodes created by antennas of the same frequency."""
    width, height = bounds
    antinodes = set()

    # If we have multiple antennas of this frequency, add all antenna positions as antinodes
    if len(positions) > 1:
        antinodes.update(positions)

    # Check every point in the grid
    for x in range(width):
        for y in range(height):
            point = (x, y)

            # Skip if it's already an antinode
            if point in antinodes:
                continue

            # Check if this point is collinear with any pair of antennas
            for i, ant1 in enumerate(positions):
                if point == ant1:  # Skip if point is an antenna
                    continue

                for j, ant2 in enumerate(positions):
                    if i >= j or point == ant2:  # Skip duplicates and antenna positions
                        continue

                    if is_collinear(ant1, point, ant2):
                        # If point is collinear with two antennas, it's an antinode
                        antinodes.add(point)
                        break

                if point in antinodes:  # If we found an antinode, move to next point
                    break

    return antinodes


def solve_antenna_problem(input_grid: str) -> int:
    """Calculate total number of unique antinode locations."""
    lines = input_grid.strip().split('\n')
    width, height = len(lines[0].strip()), len(lines)

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
