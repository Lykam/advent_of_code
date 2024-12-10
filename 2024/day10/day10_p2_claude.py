from collections import deque, defaultdict
from typing import List, Set, Tuple, Dict

def read_input(file_path: str) -> List[List[int]]:
    """Read and parse the input file into a 2D grid of integers."""
    with open(file_path, 'r') as f:
        return [[int(c) for c in line.strip()] for line in f if line.strip()]

def find_trailheads(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Find all positions with height 0 in the grid."""
    rows, cols = len(grid), len(grid[0])
    return [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

def get_neighbors(pos: Tuple[int, int], grid: List[List[int]], current_height: int) -> List[Tuple[int, int]]:
    """Get valid neighboring positions that increase height by exactly 1."""
    rows, cols = len(grid), len(grid[0])
    r, c = pos
    neighbors = []
    
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
        new_r, new_c = r + dr, c + dc
        if (0 <= new_r < rows and 0 <= new_c < cols and 
            grid[new_r][new_c] == current_height + 1):
            neighbors.append((new_r, new_c))
    
    return neighbors

def count_distinct_trails(grid: List[List[int]], start: Tuple[int, int]) -> int:
    """
    Count the number of distinct hiking trails from the start position.
    Uses dynamic programming to handle cases with multiple paths to the same position.
    """
    rows, cols = len(grid), len(grid[0])
    # dp[r, c, h] represents number of paths to position (r,c) at height h
    dp: Dict[Tuple[int, int, int], int] = defaultdict(int)
    dp[(start[0], start[1], 0)] = 1
    
    # Process heights in order from 0 to 8
    for height in range(9):
        # Find all positions with current height that have paths to them
        current_positions = [(r, c) for (r, c, h) in dp.keys() if h == height]
        
        # For each position, distribute its paths to valid neighbors
        for pos in current_positions:
            paths = dp[(pos[0], pos[1], height)]
            if paths == 0:
                continue
                
            for next_pos in get_neighbors(pos, grid, height):
                dp[(next_pos[0], next_pos[1], height + 1)] += paths
    
    # Sum up paths to all height-9 positions
    total_paths = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 9:
                total_paths += dp[(r, c, 9)]
    
    return total_paths

def solve_part2(file_path: str) -> int:
    """Solve part 2: Find sum of ratings (distinct trails) for all trailheads."""
    grid = read_input(file_path)
    trailheads = find_trailheads(grid)
    
    total_rating = 0
    for trailhead in trailheads:
        rating = count_distinct_trails(grid, trailhead)
        total_rating += rating
    
    return total_rating

if __name__ == "__main__":
    input_path = "C:/Users/PC/GitProjects/advent_of_code/2024/day10/input10.txt"
    result = solve_part2(input_path)
    print(f"Sum of trailhead ratings: {result}")
