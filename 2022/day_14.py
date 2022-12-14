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
                dir = 1 if ex > sx else -1
                for x in range(sx, ex + dir, dir):
                    rocks.add((x, sy))
            else:
                dir = 1 if ey > sy else -1
                for y in range(sy, ey + dir, dir):
                    rocks.add((sx, y))
    return rocks


def get_lowest(blocked, start):
    y = 0
    while True:
        if (start, y) in blocked:
            return start, y - 1
        y += 1


def move_to(blocked, current, max_depth, part=1):
    if part == 1 and current[1] >= max_depth:
        return None
    elif part == 2 and current[1] + 1 == max_depth:
        blocked.add(current)
        return current
    elif (current[0], current[1] + 1) not in blocked:
        return move_to(blocked, (current[0], current[1] + 1), max_depth, part=part)
    elif (current[0] - 1, current[1] + 1) not in blocked:
        return move_to(blocked, (current[0] - 1, current[1] + 1), max_depth, part=part)
    elif (current[0] + 1, current[1] + 1) not in blocked:
        return move_to(blocked, (current[0] + 1, current[1] + 1), max_depth, part=part)
    blocked.add(current)
    return current


def run_simulation(_data, start=500, part=1):
    blocked = prep_data(_data)
    count = 0
    max_y = max([rock[1] for rock in blocked])
    if part == 2:
        max_y += 2
    while True:
        current = get_lowest(blocked, start)
        if (500, 0) in blocked:
            break
        _next = move_to(blocked, current, max_depth=max_y, part=part)
        if _next is None:
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
