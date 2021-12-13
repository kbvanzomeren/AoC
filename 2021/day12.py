import os
from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from copy import copy, deepcopy

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    options = defaultdict(list)
    for line in data:
        x1, x2 = line.split('-')
        options[x1].append(x2)
        options[x2].append(x1)
    uc = [_c for _c in options.keys() if _c.isupper()]
    lc = [_c for _c in options.keys() if _c.islower()]
    return options, uc, lc


def has_valid_neighbours(current, options, uc, current_path, allow_twice=''):
    valid = []
    for c in options[current]:
        if c not in current_path:
            valid.append(c)
        elif c == allow_twice:
            if current_path.count(c) < 3:
                valid.append(c)
        elif current in uc:
            valid.append(c)
    return valid


def check_path(options, uc, lc, possible_paths=['start'], allow_twice=''):
    round = list(possible_paths)
    for current_path in round:
        current = current_path[-1]
        if current != 'end':
            for cave in options[current]:
                if cave in lc and cave in current_path or (
                        cave == allow_twice and current_path.count(cave) == 2):
                    pass
                elif cave in lc:
                    possible_paths.append(current_path + [cave])
                elif cave in uc:
                    nbs = has_valid_neighbours(cave, options, uc, current_path, allow_twice)
                    if nbs:
                        possible_paths.append(current_path + [cave])
            possible_paths.remove(current_path)
    return possible_paths


def get_possible_paths(options, uc, lc, allow_twice=''):
    _base = 'start'
    possible_paths = [['start']]
    old_paths = 1
    new_paths = 2
    while old_paths != new_paths:
        old_paths = sorted([','.join(_p) for _p in possible_paths])
        new_paths = check_path(options, uc, lc, possible_paths=possible_paths, allow_twice=allow_twice)
        new_paths = sorted([','.join(_p) for _p in new_paths])
    return possible_paths


def part1(data):
    options, uc, lc = prep_data(data)
    return len(get_possible_paths(options, uc, lc))


def part2(data):
    options, uc, lc = prep_data(data)
    visited = []
    total = 0
    for i in lc:
        if i == 'start' or i == 'end':
            continue
        iu = i.upper()
        _lc = list(lc)
        _uc = list(uc)
        _lc.remove(i)
        _uc.append(iu)
        _options = deepcopy(options)
        _options[iu] = _options.pop(i)
        for key, value in _options.items():
            if i in value:
                _options[key].remove(i)
                _options[key].append(iu)
        paths = get_possible_paths(_options, _uc, _lc, allow_twice=iu)
        for p in paths:
            _p = ','.join(p).replace(iu, i)
            if _p not in visited:
                visited.append(_p)
                total += 1
    return total


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=226, a2=3509)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
