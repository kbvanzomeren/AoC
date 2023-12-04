# from functions.load_data import load_data
import hashlib
from hashlib import md5

from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import string

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

# BLOCK = 100000
BLOCK = 100000

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

chars = ascii_lowercase + digits

triples = [c*3 for c in chars]
quins = [c*5 for c in chars]


def get_keys_indexes(salt, is_stretched=False):
    i = 1000
    last = False
    if is_stretched:
        HASHES = [''] * 1000
        for _h in [md5(f'{data}{str(j)}'.encode()).hexdigest() for j in range(BLOCK)]:
            for _ in range(2016):
                _h = md5(_h.encode()).hexdigest()
            HASHES.append(_h)
        print(HASHES[1000])
    else:
        HASHES = [''] * 1000 + [md5(f'{data}{str(j)}'.encode()).hexdigest() for j in range(BLOCK)]

    valid_indexes = []
    while True:
        check_for = []
        for q in quins:
            if q in HASHES[i]:
                check_for.append(q[0] * 3)
        for hi, h in enumerate(HASHES[i - 1000: i]):
            for cf in check_for:
                if cf in h and i - 2000 + hi not in valid_indexes:
                    is_valid = True
                    cfi = h.index(cf)
                    for t in triples:
                        if t in h and t != cf and h.index(t) < cfi:
                            is_valid = False
                    if is_valid:
                        valid_indexes.append(i - 2000 + hi)
                        print(i - 1000, i - 2000 + hi, cf, h)
                        break
        i += 1
        if i == last:
            break
        if not last and len(valid_indexes) >= 64:
            last = i + 1000
    valid_indexes.sort()
    return valid_indexes


def part1(data):
    valid_indexes = get_keys_indexes(data, False)
    return valid_indexes[63]


def part2(data):
    valid_indexes = get_keys_indexes(data, True)
    return valid_indexes[63]


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)
    #
    # file_path = INPUT_DIR + "day2a.txt"
    # data = load_data(file_path)
    data = 'jlmsuwbz'
    # data = 'abc'
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")