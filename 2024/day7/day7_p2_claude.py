def parse_input(filename):
    """Parse input file and return list of equations."""
    equations = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            test_value, numbers = line.split(': ')
            test_value = int(test_value)
            numbers = [int(x) for x in numbers.split()]
            equations.append((test_value, numbers))
    return equations


def evaluate_expression(numbers, operators):
    """Evaluate expression with given numbers and operators left-to-right."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        else:  # op == '||'
            # Convert both numbers to strings, concatenate, then back to int
            result = int(str(result) + str(numbers[i + 1]))
    return result


def can_make_value(test_value, numbers):
    """Check if test_value can be made with given numbers using +, *, and ||."""
    # Number of operators needed is one less than number of numbers
    num_operators = len(numbers) - 1

    # Now we have 3 operators (0=+, 1=*, 2=||), so we need to try 3^n combinations
    total_combinations = 3 ** num_operators

    for i in range(total_combinations):
        # Convert number to base-3 to get operator pattern
        operators = []
        num = i
        for _ in range(num_operators):
            operator_code = num % 3
            if operator_code == 0:
                operators.append('+')
            elif operator_code == 1:
                operators.append('*')
            else:  # operator_code == 2
                operators.append('||')
            num //= 3

        try:
            if evaluate_expression(numbers, operators) == test_value:
                return True
        except:
            # Skip combinations that might result in invalid numbers
            # (e.g., when concatenation would create a number too large)
            continue

    return False


def solve_calibration(filename):
    """Solve the bridge repair calibration puzzle."""
    equations = parse_input(filename)
    total = 0

    for test_value, numbers in equations:
        if can_make_value(test_value, numbers):
            total += test_value

    return total


# Run the solution
if __name__ == "__main__":
    result = solve_calibration("input7.txt")
    print(f"Total calibration result: {result}")
