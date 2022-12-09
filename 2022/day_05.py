from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    crates = {i: [] for i in range(1, 10)}
    moves = []
    for line in data:
        if '[' in line:
            line = ' ' + line
            _crates = line.replace('    ', ' [.]')[1:].split(' ')
            for i, _c in enumerate(_crates, start=1):
                if _c != '[.]':
                    crates[i].append(_c[1])
        elif "move" in line:
            moves.append([int(x) for x in re.findall(r'[0-9]+', line)])
    crates = {key: value for key, value in crates.items() if value}

    return crates, moves


def move_crates(data, model=9000):
    state, moves = prep_data(data)
    for (amount, begin, end) in moves:
        if model == 9000:
            state[end] = state[begin][:amount][::-1] + state[end]
        else:
            state[end] = state[begin][:amount] + state[end]
        state[begin] = state[begin][amount:]
    return ''.join([col[0] for _, col in state.items()])


def part1(data):
    return move_crates(data)


def part2(data):
    return move_crates(data, model=9001)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1='CMZ', a2='MCD')

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
