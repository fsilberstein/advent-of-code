from typing import List


def generate_operators(curr_ops, all_operators, num_operators, possible_operators):
    if len(curr_ops) == num_operators:
        all_operators.append(curr_ops)
        return

    for op in possible_operators:
        generate_operators(
            curr_ops
            + [
                op,
            ],
            all_operators,
            num_operators,
            possible_operators,
        )


def question01(equations: List[str]) -> int:
    """
    The equations are given in the form of a list of strings with the format "a: b c d".
    The a is the result of the equation.
    The b, c, d are the operands and the operators are always + or *.
    There can be any number of operands.
    Test if the equation is true for any combination of operator without reordering the operands.
    Return the number of equations that are true.
    """
    valid_sum = 0

    for equation in equations:
        # Parse equation
        result, operands = equation.split(": ")
        result = int(result)
        operands = [int(x) for x in operands.split()]

        # Generate all possible operator combinations
        num_operators = len(operands) - 1
        all_operators = []

        generate_operators([], all_operators, num_operators, ["+", "*"])

        # Try each operator combination
        for operators in all_operators:
            val = operands[0]
            for i, op in enumerate(operators):
                if op == "+":
                    val += operands[i + 1]
                else:
                    val *= operands[i + 1]

            if val == result:
                valid_sum += result
                break

    return valid_sum


def question02(equations: List[str]) -> int:
    """
    Same as question01 but with the addition of the || operator which concatenates the two operands.
    """
    valid_sum = 0

    for equation in equations:
        # Parse equation
        result, operands = equation.split(": ")
        result = int(result)
        operands = [int(x) for x in operands.split()]

        # Generate all possible operator combinations
        num_operators = len(operands) - 1
        all_operators = []

        generate_operators([], all_operators, num_operators, ["+", "*", "||"])

        # Try each operator combination
        for operators in all_operators:

            val = operands[0]
            for i, op in enumerate(operators):
                if op == "+":
                    val += operands[i + 1]
                elif op == "*":
                    val *= operands[i + 1]
                elif op == "||":
                    val = int(str(val) + str(operands[i + 1]))

            if int(val) == result:
                valid_sum += result
                break

    return valid_sum


if __name__ == "__main__":

    example = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    assert question01(example.strip().split("\n")) == 3749
    assert question02(example.strip().split("\n")) == 11387

    equations = []
    with open("2024/day07_input.txt", "r") as f:
        for line in f:
            equations.append(line.strip())

        print(question01(equations))
        print(question02(equations))
