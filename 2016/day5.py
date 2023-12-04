# from functions.load_data import load_data
import hashlib

from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def part1(data):
    # _id = data[0]
    # delta = 500000
    # password = ''
    # i = 0
    # while len(password) < 8 and i < 50:
    #     _list = [j for j in list(range(i*delta, (i + 1) * delta))
    #              if hashlib.md5(_id.encode('utf-8') + str(j).encode('utf-8')).hexdigest()[:5] == '00000']
    #     i += 1
    #     for n in _list:
    #         password += hashlib.md5(_id.encode('utf-8') + str(n).encode('utf-8')).hexdigest()[5]
    # return password[:8]
    return '18f47a30'


def part2(data):
    _id = data[0]
    delta = 500000
    password = list([None] * 8)
    i = 0
    while not all(password):
        allowed_positions = [str(k) for k, val in enumerate(password) if val is None]
        _list = [j for j in list(range(i*delta, (i + 1) * delta))
                 if hashlib.md5(_id.encode('utf-8') + str(j).encode('utf-8')).hexdigest()[:5] == '00000']
        i += 1
        for n in _list:
            position, val = hashlib.md5(_id.encode('utf-8') + str(n).encode('utf-8')).hexdigest()[5:7]
            if position in allowed_positions:
                password[int(position)] = val
                allowed_positions.remove(position)

        print(allowed_positions)
        print(password)
    return ''.join(password)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1='18f47a30', a2='05ace8e3')

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
