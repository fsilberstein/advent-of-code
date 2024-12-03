import re


def question01(corrupted: str) -> int:
    """
    Scan the corrupted memory for uncorrupted mul instructions.
    Do the multiplication and return the sum of all the results.
    """
    # regexp to find all pieces of mul instructions like mul(x,y)
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, corrupted)

    return sum(int(x) * int(y) for x, y in matches)


def question02(corrupted: str) -> int:
    """
    Scan the corrupted memory for uncorrupted mul instructions.
    Do the multiplication and return the sum of all the results.
    Do not multiply numbers that are preceded by a "don't"
    """
    pattern = r"(don't)|(do)|mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, corrupted)
    # print(matches)

    enabled = True
    result = 0
    for match in matches:
        if match[0] == "don't":
            enabled = False
        elif match[1] == "do":
            enabled = True
        elif enabled:
            result += int(match[2]) * int(match[3])

    return result


if __name__ == "__main__":
    assert (
        question01(
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        )
        == 161
    )
    assert (
        question02(
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        == 48
    )

    with open("2024/day03_input.txt", "r") as f:
        corrupted = f.read()

        print(question01(corrupted))
        print(question02(corrupted))
