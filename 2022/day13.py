import os

import numpy as np
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    coords = []
    folds = []
    for line in data:
        if ',' in line:
            coords.append([int(x) for x in line.split(',')])
        elif 'y=' in line:
            folds.append((1, int(line.split('y=')[-1])))
        elif 'x=' in line:
            folds.append((0, int(line.split('x=')[-1])))
    max_x = max([y for y, _ in coords])
    max_y = max([x for _, x in coords])
    sheet = np.zeros((max_y + 1, max_x + 1, ))
    for x, y in coords:
        sheet[(y, x)] = 1
    return sheet, folds


def do_fold(data, n_folds=None):
    sheet, folds = prep_data(data)
    if n_folds:
        folds = folds[:n_folds]

    for axis, ind in folds:
        if axis == 1:
            for i in range(ind):
                sheet[ind - 1 - i, :] += sheet[ind + 1 + i, :]
            sheet = sheet[:ind, :]
        if axis == 0:
            for i in range(ind):
                sheet[:, ind - 1 - i] += sheet[:, ind + 1 + i]
            sheet = sheet[:, :ind]
    return sheet


def part1(data):
    sheet = do_fold(data, 1)
    sheet[sheet > 1] = 1
    return int(sheet.sum())


def part2(data):
    sheet = do_fold(data)
    sheet[sheet > 1] = 1
    for row in sheet:
        print(''.join(['#' if c else ' ' for c in row]))


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=17, a2=None)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
