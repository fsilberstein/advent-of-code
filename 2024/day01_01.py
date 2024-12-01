from collections import Counter
from typing import List


def question01(lst1: List[int], lst2: List[int]):
    """
    Given two lists of integers, pair each element of the first list with each element of the second listm and get the difference.
    Add the difference to a running total.
    """
    total = 0

    # sort both lists, to always pair each min elements
    lst1.sort()
    lst2.sort()

    for i in range(len(lst1)):
        total += abs(lst1[i] - lst2[i])

    return total


def question02(lst1: List[int], lst2: List[int]):
    """
    This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
    Calculate a total similarity score by adding up each number in the left list after multiplying it by the number
    of times that number appears in the right list.
    """
    total = 0
    c2 = Counter(lst2)
    for i in range(len(lst1)):
        total += lst1[i] * c2[lst1[i]]

    return total


if __name__ == "__main__":
    assert question01([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 11
    assert question02([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]) == 31

    with open("2024/day01_01_input.txt", "r") as f:
        # for each line, split on "   " and add the first part to lst1 and the second part to lst2
        lst1 = []
        lst2 = []
        for line in f:
            lst1.append(int(line.split("   ")[0]))
            lst2.append(int(line.split("   ")[1]))

    print("question 01: ", question01(lst1, lst2))
    print("question 02: ", question02(lst1, lst2))
