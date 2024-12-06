def parse_map(input_map):
    grid = [list(line) for line in input_map.strip().split('\n')]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return grid, (x, y), 0
    return grid, None, None


def find_loop_positions(input_map):
    grid, start_pos, start_dir = parse_map(input_map)
    if not start_pos:
        return 0

    height, width = len(grid), len(grid[0])
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    valid_positions = 0

    def simulate_with_obstacle(obstacle_pos):
        pos, direction = start_pos, start_dir
        visited_states = set()
        steps = 0
        MAX_STEPS = height * width * 4  # Maximum possible unique states

        while steps < MAX_STEPS:
            state = (pos, direction)
            if state in visited_states:
                return True

            visited_states.add(state)
            x, y = pos
            dx, dy = moves[direction]
            next_x, next_y = x + dx, y + dy

            if not (0 <= next_x < width and 0 <= next_y < height):
                return False

            if (next_x, next_y) == obstacle_pos or grid[next_y][next_x] == '#':
                direction = (direction + 1) % 4
            else:
                pos = (next_x, next_y)

            steps += 1
        return False

    for y in range(height):
        for x in range(width):
            if (x, y) != start_pos and grid[y][x] == '.':
                if simulate_with_obstacle((x, y)):
                    valid_positions += 1

    return valid_positions


with open('input6.txt', 'r') as file:
    result = find_loop_positions(file.read())
print(f"Result: {result}")
