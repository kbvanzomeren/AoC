from math import ceil

import numpy as np
_mapper = {

}

def get_coords(n):
    root = 1
    layer = 0
    while True:
        if root ** 2 == n:
            return layer, root, [layer, layer]
        if root ** 2 > n:
            return layer, root, [layer, layer - 1]
        layer += 1
        root += 2


def part1(n):
    l, r, c = get_coords(n)
    remainder = n - r ** 2 - 1
    shift = remainder % (r - 1)
    return abs(c[0]) + abs(c[1] - shift)


def get_sum(map, x, y):
    return sum([map[x - 1][y], map[x - 1][y - 1], map[x][y - 1], map[x + 1][y - 1], map[x + 1][y], map[x + 1][y + 1], map[x][y + 1], map[x - 1][y + 1]])


def part2(n):
    mx, my = 50, 50
    _map = np.zeros([mx, my])
    x, y = mx//2, my//2
    _map[x][y] = 1
    y += 1
    _map[x][y] = 1

    dir_x = -1
    dir_y = 0

    while True:
        x += dir_x * 1
        y += dir_y * 1
        _map[x][y] = get_sum(_map, x, y)
        if _map[x][y] > n:
            return _map[x][y]

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


def test() -> None:
    # data = load_data("test_input.txt")
    # assert part1(1) == 0
    assert part1(9) == 1
    assert part1(12) == 3
    assert part1(23) == 2
    assert part1(1024) == 31
    # assert part2(data) == 12
    # print(1)


if __name__ == "__main__":
    test()

    # data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(289326)}")
    print(f"Answer to part 2 is {part2(289326)}")
