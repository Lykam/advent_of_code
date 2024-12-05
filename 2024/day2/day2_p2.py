reports = []

def get_sort_type(int_list):
    if int_list == sorted(int_list):
        return "ascending"
    elif int_list == sorted(int_list, reverse=True):
        return "descending"
    else:
        ascending_count = 0
        descending_count = 0
        for i in range(len(int_list) - 1):
            if int_list[i] > int_list[i + 1]:
                ascending_count += 1
            elif int_list[i] < int_list[i + 1]:
                descending_count += 1
        if descending_count > ascending_count:
            return "descending"
        else:
            return "ascending"

def get_differences(int_list):
    differences = []
    if get_sort_type(int_list) == 'ascending':
        for i in range(len(int_list)-1):
            differences.append(int_list[i+1] - int_list[i])
    else:
        for i in range(len(int_list)-1):
            differences.append(int_list[i] - int_list[i+1])
    return differences

with open('input2.txt', 'r') as file:
    lines = [[int(x) for x in line.strip().split()] for line in file]

for line in lines:
    reports.append({'report': line, 'sort_type': get_sort_type(line), 'differences': get_differences(line)})

safe_reports = 0

def is_safe_report(report):
    # Check if the report is safe without any removals
    if get_sort_type(report) == 'ascending':
        for i in range(len(report) - 1):
            if not (1 <= report[i + 1] - report[i] <= 3):
                return False
    elif get_sort_type(report) == 'descending':
        for i in range(len(report) - 1):
            if not (1 <= report[i] - report[i + 1] <= 3):
                return False
    else:
        return False

    return True

def can_be_safe_with_removal(report):
    for i in range(len(report)):
        # Create a new report without the i-th element
        new_report = report[:i] + report[i + 1:]
        if is_safe_report(new_report):
            return True
    return False

# Update the main loop to check for safety with the Problem Dampener
for report in reports:
    if is_safe_report(report['report']) or can_be_safe_with_removal(report['report']):
        report['safety'] = True
        safe_reports += 1
    else:
        report['safety'] = False
        print(report)


print("Safe reports: ", safe_reports)

