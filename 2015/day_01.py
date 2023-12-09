from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def part1(data):
    return data[0].count('(') - data[0].count(')')


def part2(data):
    floor = i = 0
    ins = data[0]

    while floor >= 0:
        floor += 1 if ins[i] == "(" else -1
        i += 1
    return i

    return data[0].count('(') - data[0].count(')')


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
