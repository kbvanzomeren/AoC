from time import sleep

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    return np.matrix([[x for x in line] for line in data], dtype=int)


def neighbors(data, x, y, coords_only=False):
    nb = []
    my, mx = data.shape
    for i in [x - 1, x + 1]:
        if 0 <= i < mx:
            nb.append(data[y, i])
    for j in [y - 1, y + 1]:
        if 0 <= j < my:
            nb.append(data[j, x])
    if data[y, x] < min(nb) and coords_only:
        if coords_only:
            return (y, x)
        else:
            return data[y, x] + 1
    return 0


def part1(data):
    _data = prep_data(data)
    return sum(neighbors(_data, x, y) for y, x in np.ndindex(_data.shape))


def get_valid_neighbors(current, data, bounds, coords_to_check, visited, size):
    my, mx = bounds
    y, x = current
    for i in [x - 1, x + 1]:
        if 0 <= i < mx:
            if data[y, i] != 9 and (y, i) not in visited:
                coords_to_check.append((y, i))
                visited.append((y, i))
                size += 1
    for j in [y - 1, y + 1]:
        if 0 <= j < my:
            if data[j, x] != 9 and (j, x) not in visited:
                coords_to_check.append((j, x))
                visited.append((j, x))
                size += 1
    return size


def get_basin(initial, data, bounds):
    coords_to_check = [initial]
    size = 1
    visited = []
    while coords_to_check:
        current = coords_to_check.pop(0)
        visited.append(current)
        size = get_valid_neighbors(current, data, bounds, coords_to_check, visited, size)
    return size


def part2(data):
    _data = prep_data(data)
    coords = [_c for _c in [neighbors(_data, x, y, coords_only=True) for y, x in np.ndindex(_data.shape)] if _c]
    bounds = _data.shape
    all_sizes = []
    for bc in coords:
        all_sizes.append(get_basin(bc, _data, bounds))
    return np.prod(sorted(all_sizes)[-3:])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=15, a2=1134)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
