
from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    data = np.array([[i for i in line] for line in data])
    return data.astype(dtype=int)


def build_neighbors_map(data):
    results = {}
    my, mx = data.shape
    for y, x in np.ndindex(data.shape):
        results[y, x] = [[], []]

        for i in [x - 1, x,  x + 1]:
            for j in [y - 1, y, y + 1]:
                if 0 <= i < mx and 0 <= j < my and not (x == i and y ==j):
                    results[y, x][0].append(j)
                    results[y, x][1].append(i)
    return results


def run(data, map, sum):
    items = np.argwhere(data > 9)
    while len(items):
        sum += len(items)
        for y, x in items:
            data[y, x] = -999
            data[map[y, x][0], map[y, x][1]] += 1
        items = np.argwhere(data > 9)
    data[data < 0] = 0
    return sum


def part1(data):
    _data = prep_data(data)
    _map = build_neighbors_map(_data)
    _sum = 0
    for _ in range(100):
        _data += 1
        _sum = run(_data, _map, _sum)
    return _sum


def part2(data):
    _data = prep_data(data)
    _map = build_neighbors_map(_data)
    step = 0
    while np.sum(_data):
        step += 1
        _data += 1
        _ = run(_data, _map, 0)
    return step


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1656, a2=195)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
