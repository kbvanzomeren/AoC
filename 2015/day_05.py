import time

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def passes_rules(line):
    if any([s in line for s in  ['ab', 'cd', 'pq', 'xy']]):
        return False
    if not any([i == j for i, j in zip(line[:-1], line[1:])]):
        return False
    if sum([line.count(c) for c in 'aeiou']) < 3:
        return False
    return True


def passes_rules_new(line):
    if not any([i == j for i, j in zip(line[:-2], line[2:])]):
        return False
    pairs = [i + j for i, j in zip(line[:-1], line[1:])]
    count_pairs = [pairs.count(pair) for pair in pairs]
    doubles = [pair for pair in pairs if pairs.count(pair) > 1]

    if any(pair > 2 for pair in count_pairs):
        return True
    elif any(pair == 2 for pair in count_pairs):
        if sum(p1 == p2 for p1, p2 in zip(pairs[:-1], pairs[1:])) == len(set(doubles)):
            return False
        return True
    return False


def part1(data):
    return sum(passes_rules(line) for line in data)


def part2(data):
    return sum(passes_rules_new(line) for line in data)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=2, a2=46)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
