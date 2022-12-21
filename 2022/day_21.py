from math import floor, ceil

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    operation = {}
    for line in data:
        monkey, oper = line.split(': ')
        if "+" in oper:
            operation[monkey] = (0, oper.split(' + '))
        elif "-" in oper:
            operation[monkey] = (1, oper.split(' - '))
        elif "*" in oper:
            operation[monkey] = (2, oper.split(' * '))
        elif "/" in oper:
            operation[monkey] = (3, oper.split(' / '))
        else:
            operation[monkey] = (4, int(oper))
    return operation


def get_riddle(monkeys, monkey, memo={}):
    if monkey in memo:
        return memo[monkey]
    if monkeys[monkey][0] == 4:
        memo[monkey] = monkeys[monkey][1]
        return memo[monkey]
    elif monkeys[monkey][0] == 0:
        memo[monkey] = get_riddle(monkeys, monkeys[monkey][1][0], memo) + get_riddle(monkeys, monkeys[monkey][1][1], memo)
    elif monkeys[monkey][0] == 1:
        memo[monkey] = get_riddle(monkeys, monkeys[monkey][1][0], memo) - get_riddle(monkeys, monkeys[monkey][1][1], memo)
    elif monkeys[monkey][0] == 2:
        memo[monkey] = get_riddle(monkeys, monkeys[monkey][1][0], memo) * get_riddle(monkeys, monkeys[monkey][1][1], memo)
    elif monkeys[monkey][0] == 3:
        memo[monkey] = get_riddle(monkeys, monkeys[monkey][1][0], memo) / get_riddle(monkeys, monkeys[monkey][1][1], memo)
    return memo[monkey]


def part1(data):
    monkeys = prep_data(data)
    return int(get_riddle(monkeys, "root"))


def calc_stepsizes(monkeys):
    sizes = [1]
    stepsize = 10
    monkeys["humn"] = (4, 1)
    result = {}
    get_riddle(monkeys, "root", result)
    direction = -1 if result[monkeys["root"][1][0]] < result[monkeys["root"][1][1]] else 1
    while True:
        result = {}
        monkeys["humn"] = (4, stepsize)
        get_riddle(monkeys, "root", result)
        if direction * result[monkeys["root"][1][0]] < direction * result[monkeys["root"][1][1]]:
            break
        sizes.append(stepsize)
        stepsize *= 10
    return sizes, direction


def part2(data):
    monkeys = prep_data(data)
    step_sizes, direction = calc_stepsizes(monkeys)

    i = 0
    while step_sizes:
        step_size = step_sizes.pop()
        while True:
            new_i = i + step_size
            monkeys["humn"] = (4, new_i)
            result = {}
            get_riddle(monkeys, "root", result)
            if direction * result[monkeys["root"][1][0]] < direction* result[monkeys["root"][1][1]]:
                break
            i = new_i
        if result[monkeys["root"][1][0]] == result[monkeys["root"][1][1]]:
            return i
    return i


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=152, a2=301)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
