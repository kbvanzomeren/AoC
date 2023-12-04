from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def get_code(data, postion=-1):
    matrix = np.matrix([[x for x in line] for line in data]).transpose()
    code = ''
    for p in matrix:
        pl = p.tolist()[0]
        stringy = ''.join(pl)
        pl.sort(key=lambda x: stringy.count(x))
        code += pl[postion]
    return code


def part1(data):
    return get_code(data)


def part2(data):
    return get_code(data, 0)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1='easter', a2='advent')

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
