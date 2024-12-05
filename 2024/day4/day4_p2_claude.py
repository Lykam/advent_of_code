def load_grid_from_file(filename):
    """Read the input from a file and convert it into a 2D grid."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f if line.strip()]


def find_xmas_pattern(grid):
    """Find all X-shaped patterns containing two 'MAS' sequences."""
    height = len(grid)
    width = len(grid[0])
    count = 0

    def check_mas(sequence):
        """Check if sequence is 'MAS' forwards or backwards."""
        return sequence in ['MAS', 'SAM']

    def get_sequence(row, col, direction):
        """Get 3-letter sequence in specified direction starting from given position."""
        try:
            if direction == 'down_right':
                return ''.join(grid[row + i][col + i] for i in range(3))
            elif direction == 'down_left':
                return ''.join(grid[row + i][col - i] for i in range(3))
            elif direction == 'up_right':
                return ''.join(grid[row - i][col + i] for i in range(3))
            elif direction == 'up_left':
                return ''.join(grid[row - i][col - i] for i in range(3))
        except IndexError:
            return None

    # Check each possible starting point for the X pattern
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            # Check all possible combinations of diagonal directions
            diagonal_pairs = [
                # Starting from top
                [('down_right', (row - 1, col - 1)), ('down_left', (row - 1, col + 1))],
                # Starting from bottom
                [('up_right', (row + 1, col - 1)), ('up_left', (row + 1, col + 1))],
                # Starting from left
                [('up_right', (row + 1, col - 1)), ('down_right', (row - 1, col - 1))],
                # Starting from right
                [('up_left', (row + 1, col + 1)), ('down_left', (row - 1, col + 1))]
            ]

            # Try each combination of diagonal pairs
            for pair in diagonal_pairs:
                (dir1, pos1), (dir2, pos2) = pair
                seq1 = get_sequence(*pos1, dir1)
                seq2 = get_sequence(*pos2, dir2)

                if seq1 and seq2:  # If both sequences exist
                    if check_mas(seq1) and check_mas(seq2):
                        count += 1

    return count // 4  # Divide by 4 as we're counting each X pattern from all possible starting points


def main():
    try:
        grid = load_grid_from_file('input4.txt')
        count = find_xmas_pattern(grid)
        print(f"X-MAS pattern appears {count} times in the word search")
    except FileNotFoundError:
        print("Error: input4.txt file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
