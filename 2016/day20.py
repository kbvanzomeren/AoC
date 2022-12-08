# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

def prep_data(data):
    start_ranges = []
    ranges = {}
    for line in data:
        start, end = [int(i) for i in line.split('-')]
        start_ranges.append(start)
        if start in ranges:
            print('Huh')
        ranges[start] = end

    return sorted(start_ranges), ranges


def check_ranges(s, r, first=True):
    if 0 not in s and first:
        return 0

    lower = 0
    upper = r[lower]
    free_ranges = 0
    # free_ranges = []
    while True:
        intersection = [ip for ip in s if lower + 1 <= ip <= upper + 1]
        if (not intersection or max(r[ip] for ip in intersection) <= upper) and not first:
            # s = [ip for ip in s if ip > upper + 1]
            # free_ranges.append([upper + 1, r[s[0]]])
            free_ranges += 1
            new_upper = upper + 1
        elif (not intersection or max(r[ip] for ip in intersection) <= upper) and first:
            return upper + 1
        else:
            new_upper = max(r[ip] for ip in intersection)

        lower = upper
        upper = new_upper
        if upper >= 4294967295:
            return free_ranges


def part1(data):
    s, r = prep_data(data)
    return check_ranges(s, r)


def part2(data):
    s, r = prep_data(data)
    return check_ranges(s, r, False)


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")