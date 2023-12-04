import time

from functions.generic import *
from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def part1(data):
    return min([sum([abs(i - j) for j in data]) for i in range(max(data))])


def part2(data):
    delta = {}
    old_value = 0
    for i in range(max(data) + 1):
        delta[i] = old_value + i
        old_value = delta[i]
    return min([sum([delta[abs(i - j)] for j in data]) for i in range(max(data))])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=37, a2=168, _load_data=load_data)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
