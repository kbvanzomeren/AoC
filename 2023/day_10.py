from functions.generic import *
from functions.load_data import load_data
from functions.test import test
from functions.map import add_boundary, find_start

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


ROTATION = {
    "L": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    "F": {(0, -1): (1, 0), (-1, 0): (0, 1)},
    "J": {(1, 0): (0, -1), (0, 1): (-1, 0)},
    "7": {(1, 0): (0, 1), (0, -1): (-1, 0)},
}
SURROUNDINGS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VOID = ' '


def get_initial_positions(start, grid):
    x, y = start
    options = [] # (x, y, direction_x, direction_y)
    if grid[y - 1][x] in ["F", "7", "|"]:
        options.append((x, y, 0, -1))
    if grid[y + 1][x] in ["J", "L", "|"]:
        options.append((x, y, 0, 1))
    if grid[y][x - 1] in ["F", "L", "-"]:
        options.append((x, y, -1, 0))
    if grid[y][x + 1] in ["J", "7", "-"]:
        options.append((x, y, 1, 0))
    return options


def clear_grid(grid, visited):
    new_grid = []
    for y, row in enumerate(grid):
        new_row = ''
        for x, char in enumerate(row):
            if char == "#":
                new_row += "#"
            elif (x, y) in visited:
                new_row += char
            else:
                new_row += "."
        new_grid.append(new_row)
    return new_grid


def get_pipe(data, visited):
    grid = add_boundary(data, "#")
    start = find_start(grid)
    positions = get_initial_positions(start, grid)
    routes = {0: '', 1: ''}
    visited.append(start)
    steps = 1
    for (x, y, dx, dy) in positions:
        new_x = x + dx
        new_y = y + dy

        if (new_x, new_y) in visited:
            break
        if grid[new_y][new_x] in ROTATION:
            dx, dy = ROTATION[grid[new_y][new_x]][(dx, dy)]
        visited.append((new_x, new_y))
        positions.append((new_x, new_y, dx, dy))
        routes[steps % 2] += grid[new_y][new_x]
        steps += 1
    return steps // 2, grid


def is_inside(grid):
    cnt = 0
    for y, row in enumerate(grid):
        current = 0
        for x, value in enumerate(row):
            current += value in ["|", "F", "7"]
            if current % 2 and value == '.':
                cnt += 1
    return cnt


def part1(data):
    return get_pipe(data, [])[0]


def part2(data):
    visited = []
    _, grid = get_pipe(data, visited)
    grid = clear_grid(grid, visited)
    return is_inside(grid)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
