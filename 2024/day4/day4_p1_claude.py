def load_grid_from_file(filename):
    """Read the input from a file and convert it into a 2D grid."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]


def find_xmas(grid):
    """Find all occurrences of XMAS in the grid in all directions."""
    height = len(grid)
    width = len(grid[0])
    count = 0

    # Direction vectors for all 8 possible directions
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # diagonal down-right
        (-1, 1),  # diagonal up-right
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # diagonal up-left
        (1, -1)  # diagonal down-left
    ]

    def check_word(row, col, dx, dy):
        """Check if XMAS exists starting at (row,col) in direction (dx,dy)."""
        if not (0 <= row + 3 * dx < height and 0 <= col + 3 * dy < width):
            return False

        word = ''.join(grid[row + i * dx][col + i * dy] for i in range(4))
        return word == 'XMAS'

    # Check every starting position and direction
    for row in range(height):
        for col in range(width):
            for dx, dy in directions:
                if check_word(row, col, dx, dy):
                    count += 1

    return count


def main():
    # Read and process the input file
    try:
        grid = load_grid_from_file('input4.txt')
        count = find_xmas(grid)
        print(f"XMAS appears {count} times in the word search")
    except FileNotFoundError:
        print("Error: input.txt file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
