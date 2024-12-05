left_list = []
right_list = []

similarity_score = 0

with open("input1.txt", "r") as file:
    for line in file:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

for i in left_list:
    similarity_score += i * right_list.count(i)
    print(similarity_score)

print(f"Similarity Score: {similarity_score}")
