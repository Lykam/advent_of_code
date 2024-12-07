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
        else:  # op == '*'
            result *= numbers[i + 1]
    return result


def can_make_value(test_value, numbers):
    """Check if test_value can be made with given numbers using + and *."""
    # Number of operators needed is one less than number of numbers
    num_operators = len(numbers) - 1

    # Try all possible combinations of + and *
    for i in range(2 ** num_operators):
        # Convert number to binary to get operator pattern
        operators = []
        for j in range(num_operators):
            # Use '1' for * and '0' for +
            if (i >> j) & 1:
                operators.append('*')
            else:
                operators.append('+')

        if evaluate_expression(numbers, operators) == test_value:
            return True

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
