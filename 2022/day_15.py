import re
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

REG = r'[-+]?\b\d+\b'


def prep_data(data):
    result = set()
    for line in data:
        coords = [int(x) for x in re.findall(REG, line)]
        result.add((coords[0], coords[1], coords[2], coords[3], abs(coords[0] - coords[2]) + abs(coords[1] - coords[3])))
    return result


def check_ranges(min_xs, max_xs):
    lower = min(min_xs)
    prev_upper = lower
    upper = max_xs[min_xs.index(lower)]
    x_max = max(max_xs)
    while upper < x_max:
        intersections = [max_xs[i] for i, _lower in enumerate(min_xs) if prev_upper <= _lower <= upper]
        if not intersections:
            return upper + 1
        prev_upper = upper
        upper = max(intersections)
    return None


def part1(data, loi=10):
    result = prep_data(data)
    min_xs = []
    max_xs = []
    for x, y, _, _, distance in result:
        ymoves = abs(loi - y)
        new_distance = distance - ymoves
        if new_distance > 0:
            min_xs.append(x - new_distance)
            max_xs.append(x + new_distance + 1)
    count = max(max_xs) - min(min_xs)
    visited = set()
    for _, _, x, y, _ in result:
        if y == loi and (x, y) not in visited:
            visited.add((x, y))
            count -= 1
    return count


def part2(data, max_loi=20):
    result = prep_data(data)
    current_loi = 0
    while current_loi < max_loi:
        min_xs = [] 
        max_xs = []
        for x, y, _, _, distance in result:
            ymoves = abs(current_loi - y)
            new_distance = distance - ymoves
            if new_distance > 0:
                min_xs.append(x - new_distance)
                max_xs.append(x + new_distance)
        xi = check_ranges(min_xs, max_xs)
        if xi:
            return xi * 4000000 + current_loi
        current_loi += 1


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=26, a2=56000011)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data, 2000000)}")
    print(f"Answer to part 2 is {part2(data, 4000000)}")
