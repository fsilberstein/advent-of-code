def pretty_print(grid: list[list[str]]) -> None:
    for row in grid:
        print("".join(row))
    print("\n")


def question01(grid: list[list[str]], debug=False) -> int:
    """
    The gris is a map. An arrow (^v<>) indicates the direction of movement of the patrol.
    Obstacles are marked with #.
    While no obstacle, the patrol moves in the direction of the arrow in the grid.
    When the patrol faces an obstacle, it moves to the next direction in the following order: ^, >, v, <.
    The patrol stops when they leave the grid. Mark the path of the patrol with 'X'.
    Return the number of 'X' in the grid.
    """
    grid = [list(row) for row in grid]
    rows = len(grid)
    cols = len(grid[0])

    # Find starting position (first arrow)
    start_r, start_c = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "^v<>":
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    # Direction mappings
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    next_dir = {"^": ">", ">": "v", "v": "<", "<": "^"}

    # Current position and direction
    r, c = start_r, start_c
    curr_dir = grid[r][c]

    # Mark path with X
    count = 0
    while 0 <= r < rows and 0 <= c < cols:
        # Mark current position
        if grid[r][c] != "X":
            grid[r][c] = "X"
            count += 1

        # Get next position
        dr, dc = directions[curr_dir]
        new_r, new_c = r + dr, c + dc

        # Check for obstacle
        while (0 <= new_r < rows and 0 <= new_c < cols) and grid[new_r][new_c] == "#":
            # Change direction and try again
            curr_dir = next_dir[curr_dir]
            dr, dc = directions[curr_dir]
            new_r, new_c = r + dr, c + dc

        r, c = new_r, new_c
        if debug:
            pretty_print(grid)

    return count


def question02(grid: list[list[str]], debug=False) -> int:
    """
    Question01 allows the patrol to go out of the grid.
    Find all the positions where adding an obstacle will block the patrol in a loop.
    Return the number of such positions.
    """

    def is_loop(test_grid: list[list[str]], start_r: int, start_c: int) -> bool:
        rows, cols = len(test_grid), len(test_grid[0])
        directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
        next_dir = {"^": ">", ">": "v", "v": "<", "<": "^"}

        r, c = start_r, start_c
        curr_dir = test_grid[r][c]
        visited = set()

        while 0 <= r < rows and 0 <= c < cols:
            # save each visited coordinates in a specific direction
            pos = (r, c, curr_dir)
            if pos in visited:  # Found a loop
                return True
            visited.add(pos)

            # Get next position
            dr, dc = directions[curr_dir]
            new_r, new_c = r + dr, c + dc

            # Check for obstacle
            while (0 <= new_r < rows and 0 <= new_c < cols) and test_grid[new_r][
                new_c
            ] == "#":
                curr_dir = next_dir[curr_dir]
                dr, dc = directions[curr_dir]
                new_r, new_c = r + dr, c + dc

            r, c = new_r, new_c

        return False  # Left the grid

    grid = [list(row) for row in grid]
    rows, cols = len(grid), len(grid[0])

    # Find starting position
    start_r, start_c = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in "^v<>":
                start_r, start_c = r, c
                break
        if start_r != -1:
            break

    # Try each empty position
    loop_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "." and (r != start_r or c != start_c):
                # Try placing obstacle
                grid[r][c] = "#"
                if is_loop(grid, start_r, start_c):
                    loop_count += 1
                    if debug:
                        pretty_print(grid)
                grid[r][c] = "."  # Reset

    return loop_count


if __name__ == "__main__":

    example_grid = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]
    assert question01(example_grid) == 41
    assert question02(example_grid) == 6

    grid = []
    with open("2024/day06_input.txt", "r") as f:
        for line in f:
            grid.append(line.strip())

        print(question01(grid))
        print(question02(grid))
