from collections import Counter
from typing import List


def question01(reports: List[List[int]]):
    """
    Given a list of reports, find the number of safe reports.
    A report is safe if all the numbers are all increasing or all decreasing.
    Also, every adjacent number must be different by at least 1 and at most 3.
    """
    safe = 0
    for report in reports:
        if all(
            report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] >= 1
            for i in range(len(report) - 1)
        ) or all(
            report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] >= 1
            for i in range(len(report) - 1)
        ):
            print(f"report: {report} is safe")
            safe += 1
        else:
            print(f"report: {report} is unsafe")

    print(f"Total of safe reports: {safe}")
    return safe


def question02(reports: List[List[int]]):
    """
    Same as question01 but we accept one faulty number in each report to consider it safe.
    One violation can be either a number that's too far apart, or a single element going
    the wrong direction while the rest follow the pattern.
    """
    safe = 0
    for report in reports:
        # Try removing each element one at a time and check if remaining sequence is valid
        is_safe = False

        # Check if sequence is mostly increasing with one violation
        for skip_idx in range(len(report)):
            filtered_report = report[:skip_idx] + report[skip_idx + 1 :]
            if all(
                filtered_report[i + 1] - filtered_report[i] >= 1
                and filtered_report[i + 1] - filtered_report[i] <= 3
                for i in range(len(filtered_report) - 1)
            ):
                is_safe = True
                break

        # Check if sequence is mostly decreasing with one violation
        if not is_safe:
            for skip_idx in range(len(report)):
                filtered_report = report[:skip_idx] + report[skip_idx + 1 :]
                if all(
                    filtered_report[i] - filtered_report[i + 1] >= 1
                    and filtered_report[i] - filtered_report[i + 1] <= 3
                    for i in range(len(filtered_report) - 1)
                ):
                    is_safe = True
                    break

        if is_safe:
            print(f"report: {report} is safe")
            safe += 1
        else:
            print(f"report: {report} is unsafe")

    print(f"Total of safe reports: {safe}")
    return safe


if __name__ == "__main__":
    assert (
        question01(
            [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ]
        )
        == 2
    )
    assert (
        question02(
            [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ]
        )
        == 4
    )

    with open("2024/day02_input.txt", "r") as f:
        # for each line, split on " " and build a list of lists
        lst = []
        for line in f:
            lst.append(list(map(int, line.split(" "))))

    question01(lst)
    question02(lst)
