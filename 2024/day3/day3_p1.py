import re

pattern = r"mul\(\d+,\d+\)"
num_pattern = r"\d+,\d+"
matches = []

with open('input3.txt', 'r') as file:
    for line in file:
        print(re.findall(pattern, line))
        matches.extend(re.findall(pattern, line))

number_strings = []
for match in matches:
    number_strings.append(re.findall(num_pattern, match))

numbers = []
for string in number_strings:
    numbers.append(string[0].split(','))

total = 0
for number in numbers:
    total += int(number[0]) * int(number[1])

print(total)
