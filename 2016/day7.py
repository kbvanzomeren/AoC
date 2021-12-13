import time

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    l1, l2 = [], []
    for line in data:
        l1 += [[ip.split(']')[-1] for ip in line.split('[')]]
        l2 += [[ip.split(']')[0] for ip in line.split('[')[1:]]]
    return l1, l2


def has_abba(items):
    for item in items:
        for c1, c2, c3, c4 in zip(item[:-3], item[1:-2], item[2:-1], item[3:]):
            if c1 == c4 and c2 == c3 and c1 != c2:
                return True
    return False


def has_aba(items, hyper=[], level=0, m1=None, m2=None):
    _has_aba = False
    aba_in_hype = False

    for item in items:
        for c1, c2, c3 in zip(item[:-2], item[1:-1], item[2:]):
            if c1 == c3 and c1 != c2:
                if level == 0:
                    return True
                elif level == 1:
                    if has_aba(hyper, level=2, m1=c1, m2=c2):
                        _has_aba = True
                elif level == 2:
                    if c1 == m2 and c2 == m1:
                        return True
    if aba_in_hype:
        return False

    return _has_aba


def part1(data):
    l1, l2 = prep_data(data)
    ips = 0
    for x1, x2 in zip(l1, l2):
        if has_abba(x2):
            pass
        elif has_abba(x1):
            ips += 1
    return ips


def part2(data):
    l1, l2 = prep_data(data)
    ips = 0
    for x1, x2 in zip(l1, l2):
        if not has_aba(x2,  level=0):
            pass
        elif has_aba(x1, level=0):
            if has_aba(x1, x2, level=1):
                print('Valid')
                print(x1, x2)
                ips += 1
            else:
                print('invalid')
                print(x1, x2)
    return ips


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=2, a2=3)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
