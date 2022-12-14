from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    rocks = set()
    for line in data:
        coords = line.split(' -> ')
        for start, end in zip(coords[:-1], coords[1:]):
            sx, sy = [int(x) for x in start.split(',')]
            ex, ey = [int(y) for y in end.split(',')]
            if sx != ex:
                _dir = 1 if ex > sx else -1
                for x in range(sx, ex + _dir, _dir):
                    rocks.add((x, sy))
            else:
                _dir = 1 if ey > sy else -1
                for y in range(sy, ey + _dir, _dir):
                    rocks.add((sx, y))
    return rocks


def move_to(blocked, current, max_depth, part=0):
    if part == 0 and current[1] >= max_depth:
        return None
    elif part == 2 and current[1] + 1 == max_depth:
        pass
    elif (current[0], current[1] + 1) not in blocked:
        return move_to(blocked, (current[0], current[1] + 1), max_depth, part=part)
    elif (current[0] - 1, current[1] + 1) not in blocked:
        return move_to(blocked, (current[0] - 1, current[1] + 1), max_depth, part=part)
    elif (current[0] + 1, current[1] + 1) not in blocked:
        return move_to(blocked, (current[0] + 1, current[1] + 1), max_depth, part=part)
    blocked.add(current)
    return current


def run_simulation(_data, part=0):
    blocked = prep_data(_data)
    start = (500, 0)
    count = 0
    max_y = max([rock[1] for rock in blocked]) + part
    while start not in blocked:
        if move_to(blocked, start, max_depth=max_y, part=part) is None:
            break
        count += 1
    return count


def part1(data):
    return run_simulation(data)


def part2(data):
    return run_simulation(data, part=2)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=24, a2=93)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
