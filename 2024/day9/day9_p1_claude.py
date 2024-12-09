def parse_disk_map(disk_map):
    """Convert disk map string into list of alternating file and space lengths."""
    return [int(x) for x in disk_map]


def create_block_layout(lengths):
    """Convert lengths into a list where each position contains file ID or None for space."""
    blocks = []
    file_id = 0

    for i, length in enumerate(lengths):
        # Even indices are file blocks, odd indices are spaces
        if i % 2 == 0:  # File block
            blocks.extend([file_id] * length)
            file_id += 1
        else:  # Space block
            blocks.extend([None] * length)

    return blocks


def compact_disk(blocks):
    """Move files to leftmost available space until no gaps remain."""
    while True:
        # Find rightmost file and leftmost space
        rightmost_file = len(blocks) - 1
        while rightmost_file >= 0 and blocks[rightmost_file] is None:
            rightmost_file -= 1

        leftmost_space = 0
        while leftmost_space < len(blocks) and blocks[leftmost_space] is not None:
            leftmost_space += 1

        # If no more files to move or no more spaces, we're done
        if rightmost_file < 0 or leftmost_space >= len(blocks) or leftmost_space >= rightmost_file:
            break

        # Move the file block
        blocks[leftmost_space] = blocks[rightmost_file]
        blocks[rightmost_file] = None

    return blocks


def calculate_checksum(blocks):
    """Calculate filesystem checksum based on file positions."""
    checksum = 0
    for pos, file_id in enumerate(blocks):
        if file_id is not None:
            checksum += pos * file_id
    return checksum


def solve_disk_defrag(input_string):
    """Main function to solve the disk defragmentation puzzle."""
    # Parse input into lengths
    lengths = parse_disk_map(input_string.strip())

    # Create initial block layout
    blocks = create_block_layout(lengths)

    # Compact the disk
    compacted_blocks = compact_disk(blocks)

    # Calculate and return checksum
    return calculate_checksum(compacted_blocks)


# Function to read input from file
def read_input(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


if __name__ == "__main__":
    input_data = read_input('input9.txt')
    result = solve_disk_defrag(input_data)
    print(f"The filesystem checksum is: {result}")
