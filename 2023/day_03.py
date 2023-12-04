import string
from math import prod

from functions.generic import *
from functions.map import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

filter_sym = string.digits + '.'

def check_row(digit, cur_x, row, visited, direction=1):
    for count in range(1, 1 + len(row)):
        value = row[cur_x + (direction * count)]
        if value in string.digits:
            digit = digit + value if direction > 0 else value + digit
            visited.append(cur_x + (direction * count))
            continue
        break
    return digit


def check_map(_map):
    _map = add_boundary(_map)
    symbol_coords = {(x, y): c for y, line in enumerate(_map) for x, c in enumerate(line) if c not in filter_sym}
    result_a = result_b = 0

    for (x, y), current in symbol_coords.items():
        xs, ys = [x + dx for dx in [-1, 0, 1]], [y + dy for dy in [-1, 0, 1]]
        ratios = []
        for cur_y in ys:
            visited = []
            for cur_x in xs:
                if _map[cur_y][cur_x] in string.digits and cur_x not in visited:
                    visited.append(cur_x)
                    current_digit = check_row(_map[cur_y][cur_x], cur_x, _map[cur_y], visited, -1)
                    current_digit = int(check_row(current_digit, cur_x, _map[cur_y], visited, 1))

                    result_a += current_digit
                    ratios += [current_digit] if current == "*" else []
        result_b += prod(ratios) if len(ratios) > 1 else 0

    return result_a, result_b


def part1(_map):
    return check_map(_map)[0]


def part2(_map):
    return check_map(_map)[1]


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=4361, a2=467835)

    file_path = INPUT_DIR + FILE_NAME
    _map = load_data(file_path)
    print(f"Answer to part 1 is {part1(_map)}")
    print(f"Answer to part 2 is {part2(_map)}")
