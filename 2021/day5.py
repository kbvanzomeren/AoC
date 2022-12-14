# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    coords = []
    for line in data:
        coords.append([int(i) for _coord in line.split(' -> ') for i in _coord.split(',')])
    max_coords = max(i for coord in coords for i in coord)
    return coords, max_coords, max_coords


def build_vent_map(data, diagonals=False):
    coords, max_x, max_y = prep_data(data)
    map = np.zeros((max_x + 1, max_y + 1))
    for (x1, y1, x2, y2) in coords:
        y_range = x_range = []
        if x1 != x2 and y1 != y2 and diagonals:
            dx = 1 if x1 <= x2 else -1
            dy = 1 if y1 <= y2 else -1
            x_range = range(x1, x2 + dx, dx)
            y_range = range(y1, y2 + dy, dy)
        elif x1 == x2:
            y_range = range(min(y1, y2), max(y1, y2) + 1)
            x_range = [x1] * len(y_range)
        elif y1 == y2:
            x_range = range(min(x1, x2), max(x1, x2) + 1)
            y_range = [y1] * len(x_range)
        map[y_range, x_range] += 1
    return int((map > 1).sum())


def part1(data):
    return build_vent_map(data)


def part2(data):
    return build_vent_map(data, True)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=5, a2=12)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
