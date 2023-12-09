from math import prod

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def calculate_size(l, w, h):
    side_1 = l * w
    side_2 = w * h
    side_3 = h * l
    return 2 * (side_1 + side_2 + side_3) + min([side_1, side_2, side_3])


def read_dimensions(data):
    return [(int(d) for d in line.split('x')) for line in data]


def part1(data):
    dimensions = read_dimensions(data)
    total = 0
    for (l, w, h) in dimensions:
        total += calculate_size(l, w, h)
    return total


def part2(data):
    dimensions = read_dimensions(data)
    total = 0
    for (l, w, h) in dimensions:
        total += 2 * sum(sorted([l, w, h])[:2]) + l * w * h
    return total


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=101, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
