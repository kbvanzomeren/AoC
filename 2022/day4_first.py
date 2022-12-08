from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

def prep_data(data):
    result = []
    for line in data:
        sections = re.findall(r'\d+', line)
        result.append([int(x) for x in sections])
    return result


def part1(data):
    data = prep_data(data)
    pairs = 0
    for sections in data:
        if sections[0] <= sections[2] and sections[1] >= sections[3] or sections[0] >= sections[2] and sections[1] <= sections[3]:
            pairs += 1
    return pairs


def part2(data):
    data = prep_data(data)
    overlap = 0
    for l1, u1, l2, u2 in data:
        # r2 = list(range(sections[2], sections[3] + 1))
        for _id in range(l1, u1 + 1):
            if l2 <= _id <= u2:
                overlap += 1
                break
    return overlap


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=2, a2=4)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
