# from functions.load_data import load_data
from copy import copy

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    converted_data = [[] for _ in data[0]]
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            converted_data[j].append(int(char))
    return converted_data
    # return [[d[x] for d in DIAGNOSTICS] for x in range(len(DIAGNOSTICS[0]))]


def part1(data):
    _converted = prep_data(data)
    bin_len = len(_converted[0])
    gamma = epsilon = ''
    for row in _converted:
        if sum(row) >= bin_len/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def get_binary(data, keep_max=False):
    max_len = len(data[0])
    _data = data
    o2 = co2 = ''
    not_found = True
    index = 0
    while not_found:
        _converted = prep_data(_data)
        bin_len = len(_converted[0])
        row = _converted[index]

        if sum(row) >= bin_len/2:
            o2 += '1'
            co2 += '0'
            max_char = '1'
        else:
            o2 += '0'
            co2 += '1'
            max_char = '0'

        new_data = []
        for _row in _data:
            if keep_max and _row[index] == max_char or not keep_max and _row[index] != max_char:
                new_data.append(_row)
        _data = new_data

        if index == max_len - 1:
            not_found = False
            result = [o2, co2]
        elif len(_data) == 1:
            not_found = False
            result = [_data[0], _data[0]]
        index += 1
    return result


def part2(data):
    o2 = get_binary(data, keep_max=True)[0]
    co2 = get_binary(data, keep_max=False)[1]
    return int(o2, 2) * int(co2, 2)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=198, a2=230)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
