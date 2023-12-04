# from functions.load_data import load_data
from copy import deepcopy
from hashlib import md5
from time import sleep

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')
IS_OPEN_CHAR = 'bcdef'

def get_vaults(current, salt, path):
    moves = []
    hashy = md5(f'{salt}{path}'.encode()).hexdigest()
    if 0 <= current[0] - 1 and hashy[0] in IS_OPEN_CHAR:
        # print('U')
        moves.append([[current[0] - 1, current[1]], path + 'U'])
    if current[0] + 1 <= 3 and hashy[1] in IS_OPEN_CHAR:
        moves.append([[current[0] + 1, current[1]], path + 'D'])
        # print('D')
    if 0 <= current[1] - 1 and hashy[2] in IS_OPEN_CHAR:
        moves.append([[current[0], current[1] - 1], path + 'L'])
        # print('L')
    if current[1] + 1 <= 3 and hashy[3] in IS_OPEN_CHAR:
        moves.append([[current[0], current[1] + 1], path + 'R'])
    #     print('R')
    # print(moves)
    return moves


def run_vault(salt, grid_size=4):
    vaults = [[[0, 0], '']]
    max_length = 0
    while vaults:
        # sleep(1)
        new_vaults = []
        for (current, path) in vaults:
            new_vaults += get_vaults(current, salt, path)
        # print(new_vaults)
        _new_vaults = []
        for _v in new_vaults:
            if _v[0] == [grid_size - 1, grid_size - 1]:
                if len(_v[1]) > max_length:
                    print(max_length)
                    max_length = len(_v[1])
                    print(max_length)
            else:
                _new_vaults.append(_v)
        vaults = deepcopy(_new_vaults)
    return max_length


def part1(data):
    # salt = data[0]
    salt = 'edjrjqaa'
    # salt = 'ihgpwlah'
    result = run_vault(salt, grid_size=4)
    print(result)
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")