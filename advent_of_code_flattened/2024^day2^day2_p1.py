reports = []

def check_order(int_list):
    if len(int_list) != len(set(int_list)):
        return "neither"
    elif int_list == sorted(int_list):
        return "ascending"
    elif int_list == sorted(int_list, reverse=True):
        return "descending"
    else:
        return "neither"

def safety_level(int_list):
    if check_order(int_list) == "neither":
        return 999, False

    biggest_difference = max(abs(int_list[i] - int_list[i+1]) for i in range(len(int_list)-1))
    safety = all(1 <= abs(int_list[i] - int_list[i+1]) <= 3 for i in range(len(int_list)-1))
    return biggest_difference, safety

with open('input2.txt', 'r') as file:
    lines = [[int(x) for x in line.strip().split()] for line in file]

for line in lines:
    biggest_difference, safety = safety_level(line)
    reports.append({'report': line, 'safety_level': safety, 'difference': biggest_difference})

safe_count = sum(1 for report in reports if report['safety_level'])
print(f"Safe reports: {safe_count}")
