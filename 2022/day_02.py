from functions.generic import *
from functions.load_data import load_data, load_data_split
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

_map_game = {'X': {'A': 4, 'B': 1, 'C': 7}, 'Y': {'A': 8, 'B': 5, 'C': 2}, 'Z': {'A': 3, 'B': 9, 'C': 6}}
_map_game_out = {'X': {'A': 3, 'B': 1, 'C': 2}, 'Y': {'A': 4, 'B': 5, 'C': 6}, 'Z': {'A': 8, 'B': 9, 'C': 7}}


def part1(rounds):
    return sum([_map_game[you][elf] for (elf, you) in rounds])


def part2(rounds):
    return sum([_map_game_out[out][elf] for (elf, out) in rounds])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=15, a2=12, _load_data=load_data_split)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
