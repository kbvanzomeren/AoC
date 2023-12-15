from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def rotate_grid(grid, direction=1):
    """Counterclockwise direction is -1, clockwise is 1"""
    trans_data = []
    for x, _ in enumerate(grid[0]):
        new_row = ''
        for y, row in enumerate(grid[::-1 * direction]):
            new_row += row[::direction][x]
        trans_data.append(new_row)
    return trans_data


def calc_score(grid):
    points = len(grid)
    score = 0
    for y, row in enumerate(grid):
        for r in row:
            if r == 'O':
                score += points - y
    return score


def rotate(grid, cycles):
    visited = {}
    grid = rotate_grid(grid, -1)
    i = 0
    cycle = 0
    while i < cycles:
        new_grid = []
        for y, row in enumerate(grid):
            next_pos = 0
            next_row = []
            for x, c in enumerate(row):
                if c == '.':
                    next_row.append(c)
                elif c == '#':
                    next_row.append(c)
                    next_pos = x + 1
                else:
                    next_row.append('.')
                    next_row[next_pos] = 'O'
                    next_pos += 1
            new_grid.append((''.join(next_row)))

        grid = rotate_grid(new_grid, 1)
        if i + cycle < cycles and (i % 4, ''.join(grid)) in visited:
            cycle = i - visited[(i % 4, ''.join(grid))]
            print(f"Found match after {i} moves, with cycle size {cycle}")
            i = cycles - ((4 * 1000000000 - i) % cycle)
            print(f"Jumped to {i}")
        elif i + cycle < cycles:
            visited[(i % 4, ''.join(grid))] = i
        i += 1
    grid = rotate_grid(grid, 1)

    return calc_score(grid)
def part1(data):
    return 1
    return rotate(data, 1)


def part2(data):
    # return rotate(data, 2 * 4)
    return rotate(data, 1000000000 * 4)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
