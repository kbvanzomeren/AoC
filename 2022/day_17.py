from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    results = []
    for line in data:
        results.append(line)
    return results


def get_coords(rocks, current):
    x, y = current
    if not rocks % 5:
        return [(x + i, y) for i in range(4)], x, x + 3, y + 1
    if rocks % 5 == 1:
        return [(x + 1, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1), (x + 1, y + 2)], x, x + 2, y + 3
    if rocks % 5 == 2:
        return [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1), (x + 2, y + 2)], x, x + 2, y + 3
    if rocks % 5 == 3:
        return [(x, y + i) for i in range(4)], x, x, y + 4
    if rocks % 5 == 4:
        return [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)], x, x + 1, y + 2


def valid_move(filled, move, current, rocks):
    if move == "<":
        _next = (current[0] - 1, current[1])
    if move == ">":
        _next = (current[0] + 1, current[1])
    if move == "down":
        _next = (current[0], current[1] - 1)
    coords, min_x, max_x, dy = get_coords(rocks, _next)

    if _next[1] < 0:
        return False, None, dy
    if min_x < 0 or max_x > 6:
        return False, None, dy
    for _c in coords:
        if _c in filled:
            return False, None, dy
    return True, _next, dy


def part1(data, current=(2, 3), start_y=3, rounds=2022):
    data = data[0]
    l_data = len(data)
    turn = rocks = 0
    filled = set()

    while rocks < rounds:
        move = data[turn]
        can_move, _next, dy = valid_move(filled, move, current, rocks)
        if can_move:
            current = _next
        can_move, _next, dy = valid_move(filled, "down", current, rocks)
        if can_move:
            current = _next
        else:
            coords, _, _, dy = get_coords(rocks, current)
            filled.update(coords)

            rocks += 1
            if dy + 3 > start_y:
                start_y = dy + 3
            current = (2, start_y)
        turn = (turn + 1) % l_data
    return start_y - 3


def print_map(filled, start_y, pattern_size):
    stringy = ''
    for y in range(start_y - 1, start_y - pattern_size, -1):
        row = ''
        for x in range(7):
            row += '#' if (x, y) in filled else ' '
        stringy += row
    return stringy


def part2(data, current=(2, 3), y=3, max_rocks=1000000000000):
    data = data[0]
    l_data = len(data)
    turn = rocks = 0

    filled = set()
    pattern_size = 50
    pattern = set()

    visited = {}
    _visited = set()
    addition = 0
    while rocks < max_rocks:
        move = data[turn]
        can_move, _next, dy = valid_move(filled, move, current, rocks)
        if can_move:
            current = _next

        can_move, _next, dy = valid_move(filled, "down", current, rocks)
        if can_move:
            current = _next
        else:
            coords, _, _, dy = get_coords(rocks, current)
            filled.update(coords)
            pattern.update(coords)
            y = dy + 3 if dy + 3 > y else y

            rocks += 1
            old_x = current[0]
            current = (2, y)

            if addition or rocks < pattern_size:
                pass
            elif (turn, rocks % 5, old_x) in _visited:
                stringy = print_map(filled, y, pattern_size)
                if stringy in visited:
                    delta_r = rocks - visited[stringy]["rocks"]
                    delta_y = y - visited[stringy]["y"]
                    mp = (max_rocks - rocks) // delta_r
                    rocks += delta_r * mp
                    addition = delta_y * mp
                else:
                    visited[stringy] = {"rocks": rocks, "y": y}
            else:
                _visited.add((turn, rocks % 5, old_x))
        turn = (turn + 1) % l_data
    return y - 3 + addition


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3068, a2=1514285714288)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
