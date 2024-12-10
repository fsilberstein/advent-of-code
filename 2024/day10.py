from typing import List


def bfs(grid: List[str], start_r: int, start_c: int) -> List[List[tuple[int, int]]]:
    """
    Perform BFS traversal starting from given position, moving in 4 directions.
    Returns all the paths found.
    A path is a list of tuples (row, col) with values going from 0 to 9 always incremented by 1.
    """
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    paths = []

    # queue stores: (row, col, current_path)
    queue = [(start_r, start_c, [(start_r, start_c)])]

    while queue:
        r, c, path = queue.pop(0)

        # If we reached 9, we found a complete path
        if int(grid[r][c]) == 9:
            paths.append(path)
            continue

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc

            # Check bounds
            if not (0 <= new_r < rows and 0 <= new_c < cols):
                continue

            # Check if next number is current + 1
            if int(grid[new_r][new_c]) == int(grid[r][c]) + 1:
                new_path = path + [(new_r, new_c)]
                queue.append((new_r, new_c, new_path))

    return paths


def question01(grid: List[str], debug: bool = True) -> int:
    """
    For each 0 (named trailhead), find all the paths that can be taken from there.
    The score of a trailhead is the number of 9s reachable from it.
    Return the sum of scores for each trailhead.
    """
    score = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                paths = bfs(grid, r, c)

                if debug:
                    for path in paths:
                        print(path)

                # get distinct 9s (last element of each path)
                distinct_9s = set(path[-1] for path in paths)
                score += len(distinct_9s)
    return score


def question02(grid: List[str], debug: bool = True) -> int:
    """
    For each 0 (named trailhead), find all the paths that can be taken from there.
    The rating of a trailhead is the number of distinct paths.
    Return the sum of ratings for each trailhead.
    """
    rating = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                paths = bfs(grid, r, c)
                rating += len(paths)
    return rating


if __name__ == "__main__":

    example = [
        "89010123",
        "78121874",
        "87430965",
        "96549874",
        "45678903",
        "32019012",
        "01329801",
        "10456732",
    ]

    assert question01(example, debug=False) == 36
    assert question02(example, debug=True) == 81

    grid = []
    with open("2024/day10_input.txt", "r") as f:
        for line in f:
            grid.append(line.strip())

        print(question01(grid, debug=False))
        print(question02(grid, debug=False))
