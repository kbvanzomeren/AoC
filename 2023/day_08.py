from copy import deepcopy
from itertools import product

from functions.generic import *
from functions.load_data import load_data

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def read_data(data):
    instructions = data[0]
    routes = {}
    for line in data[2:]:
        cur, _next = line.split(' = ')
        L, R = _next[1:-1].split(', ')
        routes[cur] = [L, R]
    return instructions, routes


def part1(data):
    instructions, routes = read_data(data)
    current = 'AAA'
    l = len(instructions)

    if current not in routes:
        return "Skip part 1"
    i = 0
    while current != "ZZZ":
        current = routes[current][0 if instructions[i % l] == 'L' else 1]
        i += 1
    return i


def get_least_common(x, y):
    if x > y:
        _min, _max = x, y
        current = x
    else:
        _min, _max = y, x
        current = y

    while True:
        while True:
            if current % _min == 0:
                break
            else:
                current += 1

        if current % x == 0 and current % y == 0:
            return current
        current += _min


def least_common_of_min(all_possibilities):
    all_combinations = list(product(*all_possibilities))

    _min_steps = None
    for option in all_combinations:
        result = 1
        for steps in option:
            result = get_least_common(result, steps)
        if _min_steps is None or result < _min_steps:
            _min_steps = result
    return _min_steps


def part2_first(data):
    """
    This function assumes the answer is a combination of the first "find_max" options, luckily it is the first one
    and it only repeats afterwards
    :param data:
    :return:
    """
    instructions, routes = read_data(data)
    starts = [key for key in routes.keys() if key[-1] == 'A']
    l = len(instructions)

    find_max = 1

    all_possibilities = []
    for current in starts:
        possibilities = []
        steps = 0

        while len(possibilities) < find_max:
            while current[-1] != "Z":
                current = routes[current][0 if instructions[steps % l] == 'L' else 1]
                steps += 1
            possibilities.append(steps)
            steps += 1
            current = routes[current][0 if instructions[steps % l] == 'L' else 1]
        all_possibilities.append(deepcopy(possibilities))
    return least_common_of_min(all_possibilities)


def part2(data):
    instructions, routes = read_data(data)
    starts = [key for key in routes.keys() if key[-1] == 'A']
    l = len(instructions)
    all_possibilities = []
    for current in starts:
        visited = []
        visited_i = []
        i = 0
        while True:
            current = routes[current][0 if instructions[i % l] == 'L' else 1]
            if (current, i % l) in visited:
                # Discovered a loop
                break
            if current[-1] == 'Z':
                visited.append((current, i % l))
                visited_i.append(i + 1)
            i += 1
        all_possibilities.append(deepcopy(visited_i))
    return least_common_of_min(all_possibilities)


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
