# from functions.load_data import load_data
import string

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

alphabet_dict1 = {
    i: x for i, x in enumerate(string.ascii_lowercase)
}

alphabet_dict2 = {
    x: i for i, x in enumerate(string.ascii_lowercase)
}

def prep_data(data):
    names = []
    ids = []
    checksums = []
    for line in data:
        checksums.append(line.split('[')[-1][:-1])
        _id = line.split('[')[0].split('-')[-1]
        ids.append(int(_id))
        names.append(''.join(line.split(f'-{_id}')[0].split('-')))
    return names, ids, checksums


def get_name(name, _id):
    new_name = []
    for word in name:
        new_word = ''
        for c in word:
            new_word += alphabet_dict1[(_id + alphabet_dict2[c]) % 26]
        new_name.append(new_word)
    return ''.join(new_name)


def get_value(name, _id, checksum, return_id=True):
    chars = sorted("".join(set(name)))
    _n = len(name)
    chars.sort(key=lambda x: _n - name.count(x))
    if ''.join(chars[:5]) == checksum:
        if return_id:
            return _id
        else:
            return get_name(name, _id)

    return 0


def part1(data):
    names, ids, checksums = prep_data(data)
    return sum([get_value(name, _id, checksum) for (name, _id, checksum) in zip(names, ids, checksums)])


def part2(data):
    names, ids, checksums = prep_data(data)
    for (name, _id, checksum) in zip(names, ids, checksums):
        name = get_value(name, _id, checksum, False)
        if 'north' in name:
            return _id
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1514, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
