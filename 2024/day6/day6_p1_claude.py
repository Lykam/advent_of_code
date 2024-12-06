def parse_map(input_map):
    grid = [list(line) for line in input_map.strip().split('\n')]

    # Find starting position and direction
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return grid, (x, y), 0  # 0=up, 1=right, 2=down, 3=left
    return grid, None, None


def simulate_guard_path(input_map):
    grid, pos, direction = parse_map(input_map)
    if not pos:
        return 0

    height, width = len(grid), len(grid[0])
    visited = {pos}
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left

    while True:
        x, y = pos
        dx, dy = moves[direction]
        next_x, next_y = x + dx, y + dy

        # Check if guard would leave the map
        if not (0 <= next_x < width and 0 <= next_y < height):
            break

        # Check if obstacle ahead
        if grid[next_y][next_x] == '#':
            direction = (direction + 1) % 4  # Turn right
        else:
            pos = (next_x, next_y)
            visited.add(pos)

    return len(visited)


# Read input from file
with open('input6.txt', 'r') as file:
    input_map = file.read()

result = simulate_guard_path(input_map)
print(f"Result: {result}")
