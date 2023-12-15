from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from functions.map import add_boundary, find_start
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


ROTATION = {
    "L": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    "F": {(0, -1): (1, 0), (-1, 0): (0, 1)},
    "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
    "7": {(1, 0): (0, 1), (0, -1): (-1, 0)},
}

SURROUNDING = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VOID = ' '


def get_initial_positions(start, map):
    x, y = start
    options = [] # (x, y, direction_x, direction_y)
    if map[y - 1][x] in ["F", "7", "|"]:
        options.append((x, y, 0, -1))
    if map[y + 1][x] in ["J", "L", "|"]:
        options.append((x, y, 0, 1))
    if map[y][x - 1] in ["F", "L", "-"]:
        options.append((x, y, -1, 0))
    if map[y][x + 1] in ["J", "7", "-"]:
        options.append((x, y, 1, 0))
    return options


def clear_map(map, visited):
    new_map = []

    for y, row in enumerate(map):
        new_row = ''
        for x, char in enumerate(row):
            if char == "#":
                new_row += "#"
                continue
            if (x, y) in visited:
                # new_row += "P"
                new_row += char
            else:
                new_row += "."
        new_map.append(new_row)
    return new_map

def is_in_bounds(to_check, visited, visited_outer, map, found):
    count = 0
    is_valid = True
    current_found = []
    while to_check and is_valid:
        current = to_check.pop(0)
        current_found.append(current)
        count += 1
        x, y = current
        if current in visited_outer:
            is_valid = False
            break
        if current in visited:
            continue
        for dx, dy in SURROUNDING:
            if map[y + dy][x + dx] == '.' or map[y + dy][x + dx] == VOID:
                to_check.append((x + dx, y + dy))
            elif map[y + dy][x + dx] == '#':
                is_valid = False
        visited.append(current)
    if is_valid:
        found += current_found
        return count
    else:
        visited_outer += current_found
    return 0


def get_pipe(data, visited):
    map = add_boundary(data, "#")
    start = find_start(map)
    positions = get_initial_positions(start, map)
    routes = {0: '', 1: ''}
    visited.append(start)
    steps = 1
    for (x, y, dx, dy) in positions:
        new_x = x + dx
        new_y = y + dy

        if (new_x, new_y) in visited:
            break
        if map[new_y][new_x] in ROTATION:
            dx, dy = ROTATION[map[new_y][new_x]][(dx, dy)]
        visited.append((new_x, new_y))
        positions.append((new_x, new_y, dx, dy))
        routes[steps % 2] += map[new_y][new_x]
        steps += 1
    return steps // 2, map

def part1(data):
    return get_pipe(data, [])[0]


def expand(map):
    new_map = []
    for row in map:
        new_row = ''
        for i in row:
            if i == '#':
                new_row += '##'
            elif i in ['F', '-', 'L', 'S']:
                new_row += i + '-'
            else:
                new_row += i + VOID
        new_map.append(new_row)

    final_map = [new_map[0]]
    for row1 in new_map[1:-1]:
        new_row = ''
        final_map.append(row1)
        for i in range(len(row1)):
            if row1[i] == '#':
                new_row += '#'
            elif row1[i] in ['|', 'F', '7']:
                new_row += '|'
            else:
                new_row += VOID
        final_map.append(new_row)
    final_map.append(new_map[0])
    return final_map

def part2(data):
    visited = []
    visited_outer = []
    _, map = get_pipe(data, visited)
    found = []
    clean_map = clear_map(map, visited)
    for row in clean_map:
        print(row)

    map = expand(clean_map)
    for row in map:
        print(row)

    visited = []
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char not in ['#', '.', VOID]:
                visited.append((x, y))

    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == "#" or (x, y) in visited or (x, y) in visited_outer:
                continue
            is_in_bounds([(x, y)], visited, visited_outer, map, found)
    return sum(map[y][x] == '.' for (x, y) in set(found))


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
