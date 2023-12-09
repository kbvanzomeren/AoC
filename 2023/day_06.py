from math import floor, ceil, prod

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def parse_data(data, part=1):

    if part == 1:
        times = get_numbers(data[0])
        records = get_numbers(data[1])
    else:
        times = [int(''.join(get_numbers(data[0], cast_to_int=False)))]
        records = [int(''.join(get_numbers(data[1], cast_to_int=False)))]
    return times, records


def run_games(times, records):
    result = 1
    for (time, record) in zip(times, records):
        result *= sum(s * (time - s) > record for s in range(0, time + 1))
    return result


def parabolic_solver(a, b, c):
    upper = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    lower = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    # Solves for 0, so boundaries == record but should be > record
    if upper.is_integer():
        upper -= 1
    if lower.is_integer():
        lower += 1
    return floor(upper) - ceil(lower) + 1


def solve_games(times, records):
    result = 1
    for (time, record) in zip(times, records):
        result *= parabolic_solver(1, -1 * time, record)
    return result


def part1(data):
    times, records = parse_data(data, part=1)
    return solve_games(times, records)


def part2(data):
    times, records = parse_data(data, part=2)
    return solve_games(times, records)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
    # prod([sum(s * (time - s) > record for s in range(0, time + 1)) for (time, record) in zip([7, 15, 30], [9, 40, 200])])
    # prod([sum(s * (time - s) > record for s in range(0, time + 1))
    #       for (time, record) in zip([71530], [940200])])
