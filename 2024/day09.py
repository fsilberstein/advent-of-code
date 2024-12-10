def question01(disk_map: str, debug: bool = True) -> int:
    """
    Process disk map and calculate checksum after moving digits to available spaces.
    """
    # Build initial disk state
    disk = []
    for i, count in enumerate(disk_map):
        if i % 2 == 0:
            disk.extend([str(i // 2)] * int(count))
        else:
            disk.extend(["."] * int(count))

    if debug:
        print("".join(disk))

    # Move digits right-to-left into first available space
    last_free_space = 0
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != ".":
            # Find first empty space to the left
            for j in range(last_free_space, i):
                if disk[j] == ".":
                    disk[j] = disk[i]
                    disk[i] = "."
                    last_free_space = j
                    break

    if debug:
        print("".join(disk))

    # Calculate checksum
    checksum = 0
    for i, c in enumerate(disk):
        if c == ".":
            break
        checksum += i * int(c)

    if debug:
        print(f"checksum: {checksum}")

    return checksum


def question02(disk_map: str, debug: bool = True) -> int:
    """
    Process disk map and calculate checksum after moving entire files to available spaces if possible.
    """
    # Build initial disk state
    disk = []
    files = []  # (start_index, id, size)
    free_spaces = []  # (start_index, size)
    for i, count in enumerate(disk_map):
        if i % 2 == 0:
            disk.extend([str(i // 2)] * int(count))
            files.append((len(disk) - int(count), str(i // 2), int(count)))
        else:
            disk.extend(["."] * int(count))
            free_spaces.append((len(disk) - int(count), int(count)))

    if debug:
        print("".join(disk))

    # Move entire files right-to-left into first available space
    for i in range(len(files) - 1, -1, -1):
        # Find first empty space to the left
        for j in range(len(free_spaces) - 1):
            if free_spaces[j][0] < files[i][0] and free_spaces[j][1] >= files[i][2]:
                #  move file to free space
                disk[free_spaces[j][0] : free_spaces[j][0] + files[i][2]] = (
                    files[i][1] * files[i][2]
                )
                #  replace file with empty space
                disk[files[i][0] : files[i][0] + files[i][2]] = ["."] * files[i][2]

                # update file position
                files[i] = (free_spaces[j][0], files[i][1], files[i][2])
                # update free space size
                free_spaces[j] = (
                    free_spaces[j][0] + files[i][2],
                    free_spaces[j][1] - files[i][2],
                )
                break

    if debug:
        print("".join(disk))

    # sort files by start index
    files.sort(key=lambda x: x[0])

    # Calculate checksum
    checksum = 0
    for i, f in enumerate(files):
        for j in range(f[2]):
            checksum += (f[0] + j) * int(f[1])

    if debug:
        print(f"checksum: {checksum}")

    return checksum


if __name__ == "__main__":

    example = "2333133121414131402"

    assert question01(example, debug=True) == 1928
    assert question02(example, debug=True) == 2858

    with open("2024/day09_input.txt", "r") as f:
        disk_map = f.read()

        print(question01(disk_map, debug=False))
        print(question02(disk_map, debug=False))
