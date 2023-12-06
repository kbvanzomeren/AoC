from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

val = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}


def from_snafu(number):
    value = 0
    m = 1
    for c in reversed(number):
        value += m * val[c]
        m *= 5
    return value


def to_snafu(value):
    number = '2'
    while from_snafu(number) < value:
        number += "2"
    ind = 0
    while ind < len(number):
        pre = number[:ind]
        remain = number[ind + 1:]
        old_i = '2'
        for i in val.keys():
            if from_snafu(pre + i + remain) < value:
                break
            old_i = i
        number = pre + old_i + remain
        ind += 1
    return number


def part1(data):
    _sum = 0
    for number in data:
        _sum += from_snafu(number)
    return to_snafu(_sum)


def part2(data):
    return to_snafu(2023)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1="2=-1=0", a2="1=110=")

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
