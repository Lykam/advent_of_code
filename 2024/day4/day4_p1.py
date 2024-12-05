xmas = ['X', 'M', 'A', 'S']

def check_horizontal(matrix):
    horizontal_count = 0
    for my_list in matrix:
        for i in range(len(my_list)):
            if my_list[i:i + 4] == xmas:
                # print(my_list[i:i + 4])
                horizontal_count += 1
        for i in range(len(my_list)):
            if my_list[i:i + 4] == xmas[::-1]:
                # print(my_list[i:i + 4])
                horizontal_count += 1
    return horizontal_count

def check_vertical(matrix):
    vert_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # print(matrix[i])
            if matrix[i][j:j + 4] == xmas:
                # print(matrix[i][j:j + 4])
                vert_count += 1
            elif matrix[i][j:j + 4] == xmas[::-1]:
                # print(matrix[i][j:j + 4])
                vert_count += 1
    return vert_count

def check_diagonals(matrix):
    diagonal_count = 0
    for i in range(3, len(matrix)-3):
        for j in range(3, len(matrix[i])-3):
            if matrix[i][j] == 'X':
                if matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S':
                    # print(matrix[i][j], matrix[i-1][j-1], matrix[i-2][j-2], matrix[i-3][j-3])
                    diagonal_count += 1
                elif matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
                    # print(matrix[i][j], matrix[i-1][j+1], matrix[i-2][j+2], matrix[i-3][j+3])
                    diagonal_count += 1
                elif matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S':
                    # print(matrix[i][j], matrix[i+1][j-1], matrix[i+2][j-2], matrix[i+3][j-3])
                    diagonal_count += 1
                elif matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
                    # print(matrix[i][j], matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3])
                    diagonal_count += 1
    return diagonal_count

with open("input4.txt", "r") as file:
    # Read all lines in the file
    lines = file.readlines()

matrix = [[char for char in line.strip()] for line in lines]

horizontal_count = 0
vertical_count = 0
diagonal_count = 0

horizontal_count += check_horizontal(matrix)
print(f"Horizontal count: {horizontal_count}")
vertical_count += check_vertical(matrix)
print(f"Vertical count: {vertical_count}")
diagonal_count += check_diagonals(matrix)
print(f"Diagonal count: {diagonal_count}")

count = horizontal_count + vertical_count + diagonal_count
print(count)
