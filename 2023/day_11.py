from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def read_map(data):
    expand_x = [x for x, _ in enumerate(data[0]) if "#" not in (row[x] for row in data)]
    expand_y = [y for y, row in enumerate(data) if "#" not in row]
    galaxies = [(x, y) for y, row in enumerate(data) for x, point in enumerate(row) if (data[y][x] == '#')]
    return expand_x, expand_y, galaxies


def run_calculation(data, expand_ratio):
    expand_x, expand_y, galaxies = read_map(data)
    distance = 0
    while galaxies:
        galaxy_x, galaxy_y = galaxies.pop(0)
        for (target_x, target_y) in galaxies:
            distance += abs(galaxy_x - target_x) + abs(galaxy_y - target_y)
            min_x, max_x = sorted([galaxy_x, target_x])
            min_y, max_y = sorted([galaxy_y, target_y])
            distance += expand_ratio * (sum(min_x < x < max_x for x in expand_x) +
                                        sum(min_y < y < max_y for y in expand_y))
    return distance


def part1(data):
    return run_calculation(data, 1)


def part2(data):
    return run_calculation(data, 1e6 - 1)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
