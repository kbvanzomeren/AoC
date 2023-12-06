from copy import copy

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    elves = set()
    move = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                elves.add((x, y))
                move[(x, y)] = 0
    return elves, move


def get_next_move(elf, elves, counter=0):
    x, y = elf
    coords = []
    has_elves = False
    for dx in range(x - 1, x + 2):
        for dy in range(y - 1, y + 2):
            coords.append((dx, dy))
            if (dx, dy) in elves and (dx, dy) != (x, y):
                has_elves = True
    if not has_elves:
        return False, (x, y)

    moves = ["N", "S", "W", "E"]
    moves = moves[counter:] + moves[:counter]
    for move in moves:
        if move == "N":
            nms = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
        if move == "E":
            nms = [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        if move == "S":
            nms = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        if move == "W":
            nms = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)]
        if all(nm not in elves for nm in nms):
            return True, nms[1]
    return True, (x, y)


def print_map(elves):
    xs = [elf[0] for elf in elves]
    ys = [elf[1] for elf in elves]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    for _y in range(y_min, y_max + 1):
        line = ''
        for _x in range(x_min, x_max + 1):
            if (_x, _y) in elves:
                line += '#'
            else:
                line += '.'
        print(line)
    print()


def check(elves):
    for x, y in elves:
        for dx in range(x - 1, x + 2):
            for dy in range(y - 1, y + 2):
                if (dx, dy) in elves and (dx, dy) != (x, y):
                    return False
    return True


def run(_map, c=0, rounds=10):
    elves, still_count = prep_data(_map)
    while c < rounds:
        new_elves = set()
        next_moves = {}
        final = []
        for elf in elves:
            has_moved, _next = get_next_move(elf, elves, c % 4)
            next_moves[elf] = _next
            final.append(_next)

        for current, _next in next_moves.items():
            if final.count(_next) == 1:
                new_elves.add(_next)
            else:
                new_elves.add(current)
        elves = copy(new_elves)
        c += 1
        if check(elves):
            return c + 1

    xs, ys = [elf[0] for elf in elves], [elf[1] for elf in elves]
    x_min, x_max, y_min, y_max = min(xs), max(xs), min(ys), max(ys)
    if rounds == c:
        return (abs(y_max - y_min) + 1) * (abs(x_max - x_min) + 1) - len(elves)
    return c


def part1(data):
    return run(data, rounds=10)


def part2(data):
    return run(data, rounds=1e9)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=110, a2=20)
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=20, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
