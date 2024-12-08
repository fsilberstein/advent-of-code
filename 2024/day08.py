import itertools


def question01(grid: list[list[str]], debug: bool = True) -> int:
    """
    Find positions of all the antennas materialized by a-zA-Z0-9.
    Return the number of antinodes found.
    """
    rows = len(grid)
    cols = len(grid[0])

    # store the coordinates of the antennas
    antennas = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.isalpha() or cell.isdigit():
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((i, j))

    antinodes = []

    # for each antenna, pair it with the other antennas
    for coordinates in antennas.values():
        # create pairs with all the coordinates
        for point1, point2 in list(itertools.combinations(coordinates, 2)):
            # find antinodes and check if they are in the grid
            distance = (point2[0] - point1[0], point2[1] - point1[1])

            antinode1 = (
                point1[0] - distance[0],
                point1[1] - distance[1],
            )
            if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                antinodes.append(antinode1)

            antinode2 = (
                point2[0] + distance[0],
                point2[1] + distance[1],
            )
            if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                antinodes.append(antinode2)

    antinodes = list(set(antinodes))

    if debug:
        # print grid with antinodes
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "." and (i, j) in antinodes:
                    print("#", end="")
                else:
                    print(grid[i][j], end="")
            print()

    return len(antinodes)


def question02(grid: list[list[str]], debug: bool = True) -> int:
    """
    Find positions of all the antennas materialized by a-zA-Z0-9.
    Return the number of antinodes found.
    """
    rows = len(grid)
    cols = len(grid[0])

    # store the coordinates of the antennas
    antennas = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell.isalpha() or cell.isdigit():
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((i, j))

    antinodes = []

    # for each antenna, pair it with the other antennas
    for coordinates in antennas.values():
        # create pairs with all the coordinates
        for point1, point2 in list(itertools.combinations(coordinates, 2)):
            # find antinodes and check if they are in the grid
            distance = (point2[0] - point1[0], point2[1] - point1[1])

            while 0 <= point1[0] < rows and 0 <= point1[1] < cols:
                antinodes.append(point1)
                point1 = (point1[0] - distance[0], point1[1] - distance[1])

            while 0 <= point2[0] < rows and 0 <= point2[1] < cols:
                antinodes.append(point2)
                point2 = (point2[0] + distance[0], point2[1] + distance[1])

    antinodes = list(set(antinodes))

    if debug:
        # print grid with antinodes
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "." and (i, j) in antinodes:
                    print("#", end="")
                else:
                    print(grid[i][j], end="")
            print()

    return len(antinodes)


if __name__ == "__main__":

    example = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    assert question01(example.strip().split("\n"), debug=False) == 14
    assert question02(example.strip().split("\n"), debug=False) == 34

    grid = []
    with open("2024/day08_input.txt", "r") as f:
        for line in f:
            grid.append(line.strip())

    print(question01(grid, debug=False))
    print(question02(grid, debug=False))
