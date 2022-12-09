from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def get_packet_start(datastream, len_protocol=4):
    c = 0
    while True:
        sub = datastream[c: c + len_protocol]
        if len(sub) == len(set(sub)):
            break
        c += 1
    return c + len_protocol


def part1(data):
    return get_packet_start(data[0], 4)


def part2(data):
    return get_packet_start(data[0], 14)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=7, a2=19)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
