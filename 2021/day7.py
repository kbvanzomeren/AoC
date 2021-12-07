import time

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    _list = [int(i) for i in data[0].split(',')]
    return _list


def part1(data):
    data = prep_data(data)
    sums = []
    for i in range(max(data)):
        sums.append(sum([abs(i - j) for j in data]))
    return min(sums)


def part2(data):
    data = prep_data(data)
    delta = {}
    old_value = 0
    sums = []
    for i in range(max(data) + 1):
        delta[i] = old_value + i
        old_value = delta[i]
    for i in range(max(data)):
        sums.append(sum([delta[abs(i - j)] for j in data]))
    return min(sums)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=37, a2=168)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
    # start = time.time()
    # end = time.time()
