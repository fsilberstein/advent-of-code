def question01(rules: list[list[int]], updates: list[list[int]]) -> int:
    """
    Each rule is a pair of pages. the first page must be printed before the second one.
    Each update is a list of pages that have been printed.
    Return the sum of the middle page number for all valid updates.
    """
    valid_count = 0

    for update in updates:
        valid = True
        # For each rule, check if both pages are in the update
        # If they are, make sure they're in the correct order
        for first, second in rules:
            if first in update and second in update:
                if update.index(first) > update.index(second):
                    valid = False
                    break
        if valid:
            valid_count += update[len(update) // 2]

    return valid_count


def question02(rules: list[list[int]], updates: list[list[int]]) -> int:
    """
    Each rule is a pair of pages. the first page must be printed before the second one.
    Each update is a list of pages that have been printed.
    Find invalid updates, fix them, and return the sum of the middle page number after fixing.
    """
    total = 0
    invalid_updates = []

    # Find invalid updates
    for update in updates:
        for first, second in rules:
            if first in update and second in update:
                if update.index(first) > update.index(second):
                    invalid_updates.append(update)
                    break

    for update in invalid_updates:
        # Convert to list to allow modifications
        pages = list(update)

        # Keep fixing until no more violations
        while True:
            fixed = True
            # Check each rule
            for first, second in rules:
                if first in pages and second in pages:
                    # If pages are in wrong order, swap them
                    first_idx = pages.index(first)
                    second_idx = pages.index(second)
                    if first_idx > second_idx:
                        pages[first_idx], pages[second_idx] = (
                            pages[second_idx],
                            pages[first_idx],
                        )
                        fixed = False

            if fixed:
                break

        # Add middle number after fixing
        total += pages[len(pages) // 2]

    return total


if __name__ == "__main__":

    rules = []
    updates = []
    with open("2024/day05_input_example.txt", "r") as f:
        for line in f:
            if "|" in line:
                pages = line.strip().split("|")
                rules.append((int(pages[0]), int(pages[1])))
            elif line.strip():
                pages = line.strip().split(",")
                updates.append([int(p) for p in pages])

        assert question01(rules, updates) == 143
        assert question02(rules, updates) == 123

    rules = []
    updates = []
    with open("2024/day05_input.txt", "r") as f:
        for line in f:
            if "|" in line:
                pages = line.strip().split("|")
                rules.append((int(pages[0]), int(pages[1])))
            elif line.strip():
                pages = line.strip().split(",")
                updates.append([int(p) for p in pages])

        print(question01(rules, updates))
        print(question02(rules, updates))
