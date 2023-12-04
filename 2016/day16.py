# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def extend_curve(l, c):
    while len(c) < l:
        a = str(c)
        b = str(a)[::-1]
        b = b.replace('0', 'p').replace('1', '0').replace('p', '1')
        c = a + '0' + b
    return c


def get_checksum(_data):
    while not len(_data) % 2:
        new_string = ''
        chunks = [_data[i:i+2] for i in range(0, len(_data), 2)]
        for chunk in chunks:
            if chunk in ['11', '00']:
                new_string += '1'
            else:
                new_string += '0'
        _data = new_string
    return _data



def part1(data):
    ls, curve = data[0].split(',')
    l = int(ls)
    curve = extend_curve(l, curve)

    checksum = get_checksum(curve[:l])
    return checksum


def part2(data):
    ls, curve = data[0].split(',')
    l = 35651584
    curve = extend_curve(l, curve)
    checksum = get_checksum(curve[:l])
    print(checksum)
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1='01100', a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")