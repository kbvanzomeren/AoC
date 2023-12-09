import string
from math import prod

from functions.generic import *
from functions.map import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

filter_sym = string.digits + '.'

f = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1)
}

def walk(directions):
    current = (0, 0)
    houses = [(0, 0)]
    for (dx, dy) in directions:
        x, y = current
        current = (x + dx, y + dy)
        if current not in houses:
            houses.append(current)
    return houses

def walk_with_robot(directions):
    santa = (0, 0)
    robot = (0, 0)
    houses = [(0, 0)]
    for i, (dx, dy) in enumerate(directions):
        x, y = robot if i % 2 else santa
        current = (x + dx, y + dy)
        if current not in houses:
            houses.append(current)
        if i % 2:
            robot = current
        else:
            santa = current
    return houses



def part1(data):
    directions = [f[d] for d in data[0]]
    houses = walk(directions)
    return len(houses)


def part2(data):
    directions = [f[d] for d in data[0]]
    houses = walk_with_robot(directions)
    return len(houses)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=2, a2=11)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # data = ['>']
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
