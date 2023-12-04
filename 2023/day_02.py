from math import prod

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

max_colors = {"red": 12, "green": 13, "blue": 14}

def play_game(data):
    result_a, result_b = 0, 0
    for i, line in enumerate(data):
        rounds = line.split(': ')[1].split('; ')
        is_valid = True
        round_max = {"red": 0, "green": 0, "blue": 0}
        for round in rounds:
            for color in round.split(', '):
                _n, _c = color.split(' ')
                if max_colors[_c] < int(_n):
                    is_valid = False
                round_max[_c] = max([round_max[_c], int(_n)])
        result_a += is_valid * (i + 1)
        result_b += prod(round_max.values())
    return result_a, result_b

def part1(data):
    return  play_game(data)[0]


def part2(data):
    return  play_game(data)[1]


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
