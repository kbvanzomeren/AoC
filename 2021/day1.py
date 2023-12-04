# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def get_increases(depths):
    # return sum([1 for i, j in zip(depths[:-1], depths[1:]) if i < j])
    return sum([i < j for i, j in zip(depths[:-1], depths[1:])])


def part1(data):
    return get_increases(data)


def part2(data):
    sums = [i + j + k for i, j, k in zip(data[:-2], data[1:-1], data[2:])]
    return get_increases(sums)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=7, a2=5)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)

    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")