from math import ceil

import numpy as np


def part1(n):
    x = ceil(n ** 0.5) + 2
    _map = np.zeros([x, x])
    for x in range(n+2):
        _map
    return 1


def get_sum(map, x, y):
    map[x][y] = sum([map[x - 1][y], map[x - 1][y - 1], map[x][y - 1], map[x + 1][y - 1], map[x + 1][y], map[x + 1][y + 1], map[x][y + 1], map[x - 1][y + 1]])
    print(map[x][y])


def part2():
    _map = np.zeros([100, 100])
    x, y = 50, 50
    _map[x][y] = 1
    y += 1
    _map[x][y] = 1

    dir_x = -1
    dir_y = 0

    for i in range(60):
        x += dir_x * 1
        y += dir_y * 1
        get_sum(_map, x, y)

        if dir_x == -1 and _map[x][y-1] == 0:
            dir_x = 0
            dir_y = -1
        elif dir_x == 1 and _map[x][y+1] == 0:
            dir_x = 0
            dir_y = 1
        elif dir_y == -1 and _map[x+1][y] == 0:
            dir_x = 1
            dir_y = 0
        elif dir_y == 1 and _map[x-1][y] == 0:
            dir_x = -1
            dir_y = 0

    # for line in _map:
    #     print(line)
    return 1


def test() -> None:
    # data = load_data("test_input.txt")
    # assert part1(1024) == 31
    # assert part2(data) == 12
    print(1)


if __name__ == "__main__":
    test()

    # data = load_data("input.txt")
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2()}")
