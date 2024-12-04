def bfs(
    grid: list[list[str]],
    start_r: int,
    start_c: int,
    directions: list[tuple[int, int]],
    word: str,
    rows: int,
    cols: int,
) -> list[list[tuple[int, int]]]:
    found = []
    # row, col, chars matched, direction, path
    queue = [(start_r, start_c, 1, None, [(start_r, start_c)])]

    while queue:
        r, c, matched, curr_dir, path = queue.pop(0)

        # Check if we found the full word
        if matched == len(word):
            found.append(path)
            continue

        # For first letter, try all directions
        # After that, keep going in same direction
        dirs_to_try = directions if curr_dir is None else [curr_dir]

        for dr, dc in dirs_to_try:
            new_r = r + dr
            new_c = c + dc

            # Check bounds
            if not (0 <= new_r < rows and 0 <= new_c < cols):
                continue

            # Check if next letter matches
            if grid[new_r][new_c] == word[matched]:
                queue.append(
                    (
                        new_r,
                        new_c,
                        matched + 1,
                        (dr, dc) if matched > 0 else None,
                        path + [(new_r, new_c)],
                    )
                )

    return found


def question01(grid: list[list[str]]) -> int:
    """
    Find all the instances of the word XMAS in a matrix of letters.
    The word can be in any direction, but it must be contiguous.
    Return the number of times the word is found.
    """
    # apply BFS to find all the instances of the word XMAS
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    count = 0

    # All 8 possible directions
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Try starting from each X in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                count += len(bfs(grid, i, j, directions, word, rows, cols))

    return count


def question02(grid: list[list[str]]) -> int:
    """
    Find all the instances of the word MAS written twice in the shape of ab X in a matrix of letters.
    Return the number of times the word is found.
    """

    #  first find all the instances of the word MAS and get the paths
    #  then for each path, check if there is another path with the "A" in the middle matching

    rows = len(grid)
    cols = len(grid[0])
    word = "MAS"
    paths = {}
    count = 0

    # Only diagonals
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Try starting from each X in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                found = bfs(grid, i, j, directions, word, rows, cols)

                for path in found:
                    # use the A coordinates to store all the path sharing the same A
                    if path[1] not in paths:
                        paths[path[1]] = []
                    paths[path[1]].append(path)

    for k in paths:
        if len(paths[k]) == 2:
            count += 1

    return count


if __name__ == "__main__":
    assert (
        question01(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 18
    )
    assert (
        question02(
            [
                "MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX",
            ]
        )
        == 9
    )

    grid = []
    with open("2024/day04_input.txt", "r") as f:
        for line in f:
            grid.append(line.strip())

        print(question01(grid))
        print(question02(grid))
