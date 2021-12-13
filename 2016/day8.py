
from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
import numpy as np
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

# rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1


def prep_data(data):
    result = []
    for line in data:
        y, x = re.findall(r'\d+', line)
        if 'rect ' in line:
            _type = 0
        if 'rotate column ' in line:
            _type = 1
        if 'rotate row ' in line:
            _type = 2
        result.append([_type, int(y), int(x) ])
    return result


def part1(data, w=7, l=3):
    display = np.zeros((l, w))
    commands = prep_data(data)
    for _type, ind, val in commands:
        # print(_type, ind, val)
        if _type == 0:
            display[0:val, 0:ind] = 1
        elif _type == 1:
            display[:, ind] = np.array(list(display[-1 * val:, ind]) + list(display[: -1 * val, ind]))
        elif _type == 2:
            # print(list(display[ind, -1 * val:]) + list(display[ind, :val]))
            display[ind, :] = np.array(list(display[ind, -1 * val:]) + list(display[ind, : -1 * val]))
            # print(np.array([display[ind, -1 * ((i + val) % w)] for i in range(w)]))
            # display[ind, :] = np.array([display[ind, -1 * (i + val) % w] for i in range(w)])
    return int(display.sum())


def part2(data, w=7, l=3):
    display = np.zeros((l, w))
    commands = prep_data(data)
    for _type, ind, val in commands:
        if _type == 0:
            display[0:val, 0:ind] = 1
        elif _type == 1:
            display[:, ind] = np.array(list(display[-1 * val:, ind]) + list(display[: -1 * val, ind]))
        elif _type == 2:
            display[ind, :] = np.array(list(display[ind, -1 * val:]) + list(display[ind, : -1 * val]))
    for row in display:
        print(''.join(['#' if _c else ' ' for _c in row]))
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=6, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data, 50, 6)}")
    print(f"Answer to part 1 is {part2(data, 50, 6)}")
