from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    coords = set()
    for line in data:
        x, y, z = line.split(',')
        coords.add((int(x), int(y), int(z)))
    return coords


SIDES = [
    lambda x, y, z: (x + 1, y, z),
    lambda x, y, z: (x - 1, y, z),
    lambda x, y, z: (x, y + 1, z),
    lambda x, y, z: (x, y - 1, z),
    lambda x, y, z: (x, y, z + 1),
    lambda x, y, z: (x, y, z - 1),
]


def part1(data):
    free_sides = 0
    coords = prep_data(data)
    for coord in coords:
        free_sides += sum([side(*coord) not in coords for side in SIDES])
    return free_sides


def part2(data):
    free_sides = 0
    occurence = defaultdict(int)
    coords = prep_data(data)
    for coord in coords:
        possible_sides = [side(*coord) for side in SIDES if side(*coord) not in coords]
        for ps in possible_sides:
            free_sides += 1
            occurence[ps] += 1
    max_size = len(coords) // 2
    pockets = set()
    for k, v in occurence.items():
        currents = [k]
        pocket = {k}
        while True:
            open_coords = []
            for _c in currents:
                possible_sides = [side(*_c) for side in SIDES]
                for ps in possible_sides:
                    if ps not in coords and ps not in pocket:
                        pocket.add(ps)
                        open_coords.append(ps)

            if len(open_coords) > max_size:
                break

            if not open_coords:
                pockets.update(pocket)
                break
            currents = open_coords
    return sum(occ for coord, occ in occurence.items() if coord not in pockets)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=64, a2=58)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
