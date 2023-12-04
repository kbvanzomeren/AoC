import time
from collections import OrderedDict
from copy import deepcopy, copy

import numpy as np

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    return [[int(x) for x in line] for line in data]


def neighbors2(path, my, mx, visited):
    y, x = path
    nb = []
    for i in [x - 1, x + 1]:
        if 0 <= i <= mx:
            nb.append((y, i))
    for j in [y - 1, y + 1]:
        if 0 <= j <= my:
            nb.append((j, x))
    return [_nb for _nb in nb if _nb not in visited]


def get_path2(_map):
    bounds = (len(_map) - 1, len(_map[0]) - 1)
    my, mx = bounds
    paths = {(0, 0): 0}
    path = (0, 0)
    value = paths.pop(path)
    visited = []
    while path != bounds:
        visited.append(path)
        nbs = neighbors2(path, my, mx, visited)
        for ny, nx in nbs:
            visited.append((ny, nx))
            val = value + _map[ny][nx]
            # if (ny, nx) in paths and val < paths[(ny, nx)]:
            #     paths[(ny, nx)] = val
            # if (ny, nx) not in paths:
            paths[(ny, nx)] = val
        path = min(paths, key=paths.get)
        value = paths.pop(path)
    return value


def part1(data):
    _map = prep_data(data)
    return get_path2(_map)


def part2(data):
    _map = prep_data(data)
    _new_map = [[] for _ in range(len(_map) * 5)]
    for dy in range(5):
        for dx in range(5):
            for ri, _row in enumerate(_map):
                _new_map[ri + len(_map) * dy] += [i + dx + dy for i in _row]

    for row in _new_map:
        for x, val in enumerate(row):
            if val > 9:
                row[x] -= 9
    return get_path2(_new_map)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=40, a2=315)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")