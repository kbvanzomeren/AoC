from defaultlist import defaultlist
from functions.generic import *
from functions.load_data import load_data
from functions.test import test


INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def calc_inv(data, return_max=1, elf=0):
    prep_data = [int(x) if x != '' else 0 for x in data]
    inventories = defaultlist(int)
    for line in prep_data:
        inventories[elf] += line
        elf += not line
    inventories.sort(reverse=True)
    return sum(inventories[:return_max])


def part1(data):
    return calc_inv(data)


def part2(data):
    return calc_inv(data, 3)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=24000, a2=45000)

    input_data = load_data(INPUT_DIR + FILE_NAME)
    print(f"Answer to part 1 is {part1(input_data)}")
    print(f"Answer to part 2 is {part2(input_data)}")
