from functions.generic import *
from functions.load_data import load_data, load_data_split_empty
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def rotate_grid(grid):
    trans_data = ['' for _ in range(len(grid[0]))]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            trans_data[x] += c
    return trans_data


def scan_valley(data, part=1):
    score = 0
    for grid in data:
        not_found, multiplier, counter = True, 100, 0
        while not_found:
            i, j, smudge = counter, counter + 1, 0
            while True:
                if grid[i] != grid[j]:
                    smudge += sum(ci != cj for ci, cj in zip(grid[i], grid[j]))
                    if part == 1 or smudge > 1:
                        break
                i -= 1
                j += 1
                if (part == 1 or smudge == 1) and (i < 0 or j == len(grid)):
                    not_found = False
                    score += multiplier * (counter + 1)
                    break
                elif i < 0 or j == len(grid):
                    break

            counter += 1
            if counter == len(grid) - 1:
                grid = rotate_grid(grid)
                counter = 0
                multiplier = 1
    return score

def part1(data):
    return scan_valley(data, part=1)


def part2(data):
    return scan_valley(data, part=2)


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2, _load_data=load_data_split_empty)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split_empty(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
