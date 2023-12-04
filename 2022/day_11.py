import math
from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data, load_data_split_empty
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

REG = r'[-+]?\b\d+\b'


def get_operation(line):
    operation = line.split(' = ')[-1]
    if 'old * old' == operation:
        return lambda old: old * old
    elif 'old *' in operation:
        con = int(operation.split(' ')[-1])
        return lambda old: old * con
    else:
        con = int(operation.split(' ')[-1])
        return lambda old: old + con


def prep_data(data):
    monkeys = []
    modu = 1
    for monkey_line, start_line, operation_line, test_line, true_line, false_line in data:
        monkey = [int(x) for x in re.findall(REG, monkey_line)][0]
        items = [int(x) for x in re.findall(REG, start_line)]
        operation = get_operation(operation_line)
        condition = [int(x) for x in re.findall(REG, test_line)][0]
        true = [int(x) for x in re.findall(REG, true_line)][0]
        false = [int(x) for x in re.findall(REG, false_line)][0]
        modu *= condition
        monkeys.append([monkey, items, operation, condition, true, false, 0])
    return monkeys, modu


def get_max_activity(monkeys, rounds, modu, divider=3):
    for i in range(rounds):
        for monkey, items, operation, condition, true, false, throw in monkeys:
            for val in items:
                monkeys[monkey][-1] += 1
                val = (operation(val) // divider) % modu
                throw_to = false if val % condition else true
                monkeys[throw_to][1].append(val)
            monkeys[monkey][1] = []
    return math.prod(sorted([monkey[-1] for monkey in monkeys])[-2:])


def part1(data):
    monkeys, modu = prep_data(data)
    return get_max_activity(monkeys, 20, modu)


def part2(data):
    monkeys, modu = prep_data(data)
    return get_max_activity(monkeys, 10000, modu, 1)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=10605, a2=2713310158, _load_data=load_data_split_empty)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split_empty(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
