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


def get_file_spans(blocks):
    """Get the start position and length of each file in the blocks."""
    file_spans = {}  # {file_id: (start_pos, length)}
    current_file = None
    start_pos = 0
    length = 0

    for pos, file_id in enumerate(blocks):
        if file_id != current_file:
            if current_file is not None:
                file_spans[current_file] = (start_pos, length)
            current_file = file_id
            start_pos = pos
            length = 1
        else:
            length += 1

    # Don't forget the last file
    if current_file is not None:
        file_spans[current_file] = (start_pos, length)

    return file_spans


def find_leftmost_space(blocks, required_length, min_pos=0):
    """Find the leftmost continuous space of required length."""
    space_start = None
    space_length = 0

    for pos in range(min_pos, len(blocks)):
        if blocks[pos] is None:
            if space_start is None:
                space_start = pos
            space_length += 1
            if space_length >= required_length:
                return space_start
        else:
            space_start = None
            space_length = 0

    return None


def compact_disk_whole_files(blocks):
    """Move whole files to leftmost available space in decreasing file ID order."""
    # Get file spans
    file_spans = get_file_spans(blocks)

    # Process files in decreasing ID order
    for file_id in sorted(file_spans.keys(), reverse=True):
        start_pos, length = file_spans[file_id]

        # Find leftmost space that can fit this file
        new_pos = find_leftmost_space(blocks, length, 0)

        # If we found a suitable space and it's to the left of the current position
        if new_pos is not None and new_pos < start_pos:
            # Move the whole file
            file_blocks = [file_id] * length
            space_blocks = [None] * length

            # Place the file in its new position
            blocks[new_pos:new_pos + length] = file_blocks
            # Clear the old position
            blocks[start_pos:start_pos + length] = space_blocks

    return blocks


def calculate_checksum(blocks):
    """Calculate filesystem checksum based on file positions."""
    checksum = 0
    for pos, file_id in enumerate(blocks):
        if file_id is not None:
            checksum += pos * file_id
    return checksum


def solve_disk_defrag_part2(input_string):
    """Main function to solve part 2 of the disk defragmentation puzzle."""
    # Parse input into lengths
    lengths = parse_disk_map(input_string.strip())

    # Create initial block layout
    blocks = create_block_layout(lengths)

    # Compact the disk using whole-file movement
    compacted_blocks = compact_disk_whole_files(blocks)

    # Calculate and return checksum
    return calculate_checksum(compacted_blocks)


# Function to read input from file
def read_input(filename):
    with open(filename, 'r') as file:
        return file.read().strip()


if __name__ == "__main__":
    input_data = read_input('input9.txt')
    result = solve_disk_defrag_part2(input_data)
    print(f"The filesystem checksum for part 2 is: {result}")
