from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')
# l1 = lower bound elf 1, u1 = upper bound elf 1


def prep_data(data):
    return [[int(x) for x in re.findall(r'\d+', line)] for line in data]


def part1(data):

    return sum([l1 <= l2 and u1 >= u2 or l1 >= l2 and u1 <= u2 for (l1, u1, l2, u2) in prep_data(data)])


def part2(data):
    return sum([u1 >= l2 and l1 <= u2 for (l1, u1, l2, u2) in prep_data(data)])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=2, a2=4)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
