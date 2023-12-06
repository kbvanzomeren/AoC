from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


BLIZ = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def prep_data(data):
    blizzards = []
    blizzards_coords = set()
    for y, line in enumerate(data):
        for x, b in enumerate(line):
            if b in BLIZ:
                blizzards.append((BLIZ[b][0], BLIZ[b][1], x, y))
                blizzards_coords.add((x, y))
    return blizzards, blizzards_coords


def possible_directions(current, blizzards, w, h, end):
    x, y = current
    moves = []
    if current not in blizzards:
        moves.append(current)
    if 0 < y - 1 and (x, y - 1) not in blizzards or (x, y - 1) == end:
        moves.append((x, y - 1))
    if x + 1 < w and y != 0 and (x + 1, y) not in blizzards:
        moves.append((x + 1, y))
    if y + 1 < h and ((x, y + 1) not in blizzards) or (x, y + 1) == end:
        moves.append((x, y + 1))
    if 0 < x - 1 and y != h and (x - 1, y) not in blizzards:
        moves.append((x - 1, y))
    return moves


def run_blizzards(blizzards, w, h):
    new_blizzards = []
    blizzards_coords = set()
    for dx, dy, x, y in blizzards:
        _x = x + dx
        _y = y + dy
        if _y == 0:
            _y = h - 1
        if _x == w:
            _x = 1
        if _y == h:
            _y = 1
        if _x == 0:
            _x = w - 1
        new_blizzards.append((dx, dy, _x, _y))
        blizzards_coords.add((_x, _y))
    return new_blizzards, blizzards_coords


def run(data, counter=1, steps=0, back=0):
    h, w = len(data) - 1, len(data[0]) - 1
    blizzards, blizzards_coords = prep_data(data)
    start = (1, 0)
    positions = {start}
    end = (w - 1, h)

    while True:
        steps += 1
        blizzards, blizzards_coords = run_blizzards(blizzards, w, h)
        new_positions = set()
        for c in positions:
            new_positions.update(possible_directions(c, blizzards_coords, w, h, end))

        positions = new_positions
        if end in positions:
            back += 1
            if back == counter:
                break
            start, end = end, start
            positions = {start}
    return steps


def part1(data):
    return run(data, counter=1)


def part2(data):
    return run(data, counter=3)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=18, a2=54)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
