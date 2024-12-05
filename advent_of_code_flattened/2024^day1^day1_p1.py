left_list = []
right_list = []

with open("input1.txt", "r") as file:
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

i = 0
total_distance = 0

while i < len(left_sorted) and i < len(right_sorted):
    if left_sorted[i] > right_sorted[i]:
        total_distance += left_sorted[i] - right_sorted[i]
    else:
        total_distance += right_sorted[i] - left_sorted[i]
    i += 1
print("Total Distance: ", total_distance)
