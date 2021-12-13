# from functions.load_data import load_data
from copy import copy

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    return [[int(x) for x in line.split('  ') if x] for line in data]


def prep_data2(data):
    _data = []
    for i in range(len(data) // 3):
        l1 = [int(x) for x in data[i * 3].split('  ') if x]
        l2 = [int(x) for x in data[i * 3 + 1].split('  ') if x]
        l3 = [int(x) for x in data[i * 3 + 2].split('  ') if x]
        for j in range(3):
            _data.append([l1[j], l2[j], l3[j]])
    return _data


def check_line(x1, x2, x3):
    return x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1


def part1(data):
    return sum([check_line(x1, x2, x3) for (x1, x2, x3) in prep_data(data)])


def part2(data):
    # prep_data2(data)
    return sum([check_line(x1, x2, x3) for (x1, x2, x3) in prep_data2(data)])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3, a2=6)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")

