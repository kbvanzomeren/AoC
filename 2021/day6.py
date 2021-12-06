
from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    fishes = [0] * 9
    for number in data[0].split(','):
        fishes[int(number)] += 1
    return fishes


def simulation_old(data, days):

    _data = data[0].split(',')
    fishes = np.array(_data, dtype=int)
    for i in range(days):
        new_fish = fishes[fishes == 0]
        fishes[fishes == 0] = 7
        fishes -= 1
        fishes = np.append(fishes, [8] * len(new_fish))
    return fishes


def simulation(fishes, days):
    for _ in range(days):
        new_fishes = [0] * 9
        for fish, count in enumerate(fishes):
            if fish == 0:
                born_fishes = re_fishes = count
                print(born_fishes)
            else:
                new_fishes[fish - 1] = count
        new_fishes[8] += born_fishes
        new_fishes[6] += re_fishes
        fishes = new_fishes
    return sum(fishes)


def part1(data):
    fishes = prep_data(data)
    return simulation(fishes, 80)


def part2(data):
    fishes = prep_data(data)
    return simulation(fishes, 256)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=5934, a2=26984457539)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
