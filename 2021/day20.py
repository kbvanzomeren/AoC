from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data, is_test=True):
    _data = []
    algo = ''
    if is_test:
        for line in data[:7]:
            algo += line.replace('.', '0').replace('#', '1')
            ind = 8
    else:
        algo = data[0].replace('.', '0').replace('#', '1')
        ind = 2
    for line in data[ind:]:
        line = line.replace('.', '0')
        line = line.replace('#', '1')
        _data.append([x for x in line])

    _map = np.array(_data)
    return algo, _map


def get_surrounding(y, x):
    return [y - 1, y - 1, y - 1, y , y, y, y + 1, y + 1, y + 1], [x - 1, x, x + 1, x - 1, x, x + 1, x - 1, x, x + 1]


def build_surrounding_map(_map):
    my, mx = _map.shape
    surrounding_map = {}
    for y in range(1, my - 1):
        for x in range(1, mx - 1):
            surrounding_map[(y, x)] = get_surrounding(_map, y, x)
    return surrounding_map


def get_inv_map(_map):
    _map_inv = np.array(_map, copy=True)
    where_0 = np.where(_map_inv == '0')
    where_1 = np.where(_map_inv == '1')
    _map_inv[where_0] = '1'
    _map_inv[where_1] = '0'
    return _map_inv


def print_map(_map):
    for row in _map:
        r = ''.join(row).replace('0', '.').replace('1', '#')
        print(r)


def part1(data, is_test=True):
    algo,_map = prep_data(data, is_test)
    # nb_map = build_surrounding_map(_map)
    i = 0
    _map = np.pad(_map, 102, mode='constant')
    _map[_map == 0] = '0'

    while i < 50:
        my, mx = _map.shape
        _map2 = np.array(_map, copy=True)
        for y in range(1, my - 1):
            for x in range(1, mx - 1):
                nbs = get_surrounding(y, x)
                value = int(''.join(_map2[(nbs)]), 2)
                _map[(y, x)] = algo[value]
        i += 1
        cut = 1
        _map = _map[cut: -cut, cut: -cut]
        if i % 2:
            _map[_map == 0] = '1'
        else:
            _map[_map == 0] = '0'
        print_map(_map)

    _map3 = _map[cut: -cut, cut: -cut]
    print_map(_map3)
    return len(_map3[_map3 == '1'])


def part2(data):
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3351, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data, is_test=False)}")
    # print(f"Answer to part 2 is {part2(data)}")
