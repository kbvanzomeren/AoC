from functions.generic import *
from functions.load_data import LoadData
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def solve_seq(line, part):
    results = [line]
    while sum(x != 0 for x in line) != 0:
        next_line = []
        for i, j in zip(line[:-1], line[1:]):
            next_line.append(j - i)
        line = next_line
        results.append(next_line)

    value = 0
    for row in results[::-1]:
        value = value + row[-1] if part == 1 else row[0] - value
    return value


def part1(data):
    return sum(solve_seq(line, 1) for line in data)


def part2(data):
    return sum(solve_seq(line, 2) for line in data)


if __name__ == "__main__":
    loader = LoadData(file="./inputs_test/" + FILE_NAME, method="int_arrays")
    test(file_name=FILE_NAME, data=loader.read(), part1=part1, part2=part2, a1=1, a2=2)

    loader.file = INPUT_DIR + FILE_NAME
    data = loader.read()
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
