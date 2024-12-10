from collections import deque
from typing import List, Set, Tuple

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

def find_reachable_nines(grid: List[List[int]], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """Find all height-9 positions reachable via valid hiking trails from the start position."""
    reachable_nines = set()
    visited = set()
    queue = deque([(start, 0)])  # (position, current_height)
    
    while queue:
        pos, height = queue.popleft()
        
        if height == 9:
            reachable_nines.add(pos)
            continue
            
        for next_pos in get_neighbors(pos, grid, height):
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, height + 1))
    
    return reachable_nines

def solve_part1(file_path: str) -> int:
    """Solve part 1: Find sum of scores for all trailheads."""
    grid = read_input(file_path)
    trailheads = find_trailheads(grid)
    
    total_score = 0
    for trailhead in trailheads:
        reachable_nines = find_reachable_nines(grid, trailhead)
        total_score += len(reachable_nines)
    
    return total_score

if __name__ == "__main__":
    input_path = "C:/Users/PC/GitProjects/advent_of_code/2024/day10/input10.txt"
    result = solve_part1(input_path)
    print(f"Sum of trailhead scores: {result}")
