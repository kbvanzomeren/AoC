from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import hashlib

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

def part1(data):
    key = data[0]
    i = 1
    while True:
        to_hash = key + str(i)
        _hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
        if _hash[:5] == '00000':
            break
        i += 1
    return i


def part2(data):
    key = data[0]
    i = 1
    while True:
        to_hash = key + str(i)
        _hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()
        if _hash[:6] == '000000':
            break
        i += 1

    return i


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1048970, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
