from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    return [[int(t) for t in line] for line in data]


def get_line_of_sight(forest, x, y):
    row = forest[y]
    left, right = row[:x][::-1], row[x + 1:]
    column = [_row[x] for _row in forest]
    up, down = column[:y][::-1], column[y + 1:]
    return left, up, right, down


def check_for_trees(forest):
    height, width = len(forest) - 1, len(forest[0]) - 1
    count = 0
    for y, row in enumerate(forest):
        for x, h in enumerate(row):
            if x == 0 or y == 0 or y == height or x == width:
                count += 1
            else:
                left, up, right, down = get_line_of_sight(forest, x, y)
                count += h and (h > max(left) or h > max(right) or h > max(up) or h > max(down))
    return count


def part1(data):
    forest = prep_data(data)
    check_for_trees(forest)
    return check_for_trees(forest)


def get_line_score(line, h):
    line_count = 0
    for _h in line:
        line_count += 1
        if _h >= h:
            return line_count
    return line_count


def get_score(forest, x, y, own_height):
    left, up, right, down = get_line_of_sight(forest, x, y)
    multi = 1
    for line in [left, up, right, down]:
        multi *= get_line_score(line, own_height)
    return multi


def part2(data):
    forest = prep_data(data)
    height, width = len(forest) - 1, len(forest[0]) - 1
    scores = []
    for y, row in enumerate(forest):
        for x, h in enumerate(row):
            if not x == 0 or y == 0 or y == height or x == width:
                scores.append(get_score(forest, x, y, h))
    return max(scores)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=21, a2=8)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
