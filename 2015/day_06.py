from math import floor, ceil, prod

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def parse_data(data):
    result = []
    for line in data:
        instruction = "on"
        if "toggle" in line:
            instruction = "toggle"
        elif "off" in line:
            instruction = "off"
        ranges = get_numbers(line)
        result.append((instruction, ranges))
    return result


def part1(data):
    data = parse_data(data)
    grid = [[False for _ in range(1000)] for _ in range(1000)]
    for (instruction, (min_x, min_y, max_x, max_y)) in data:
        new_value = instruction == "on"
        for y in range(min_y, max_y + 1):
            row = grid[y]
            for x in range(min_x, max_x + 1):
                if instruction == "toggle":
                    row[x] = not row[x]
                else:
                    row[x] = new_value
    return sum(sum(row) for row in grid)


def part2(data):
    data = parse_data(data)
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    brightness = {"off": -1, "on": 1, "toggle": 2, }
    for (instruction, (min_x, min_y, max_x, max_y)) in data:
        add_brightness = brightness[instruction]
        for y in range(min_y, max_y + 1):
            row = grid[y]
            for x in range(min_x, max_x + 1):
                if instruction == "off" and not row[x]:
                    continue
                row[x] += add_brightness
    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
