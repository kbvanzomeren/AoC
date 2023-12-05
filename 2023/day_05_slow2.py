from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


import re
result = re.findall(r'[-+]?\d*(?:.\d+)?', "hello 42 I'm a -32 string 30")
print(result)

def parse_data(data):
    results = []
    seeds = [int(s) for s in data[0].split(': ')[1].split(' ')]
    range_seeds = []
    s, r = 0, 1
    while r <= len(seeds):
        range_seeds += list(range(seeds[s], seeds[s] + seeds[r]))
        s += 2
        r += 2

    _current_map = []
    for line in data[2:]:
        if line == '':
            continue
        elif "map" in line:
            if _current_map:
                results.append(list(_current_map))
            _current_map = []
        else:
            des, source, _range = [int(n) for n in line.split(' ')]
            _current_map.append([(source, source + _range), (des)])
    results.append(list(_current_map))
    return range_seeds, results

def part1(data):
    seeds, _rounds = parse_data(data)
    numbers = seeds
    journey = [[s] for s in seeds]
    for _round in _rounds:
        print("New ro")
        new_numbers = []
        for i, n in enumerate(numbers):
            found = False

            for ((_min, _max), des) in _round:
                if found:
                    break
                if _min <= n < _max:
                    found = True
                    new_numbers.append(n - _min + des)
                    journey[i].append(n - _min + des)

            if not found:
                new_numbers.append(n)
                journey[i].append(n)
        numbers = list(new_numbers)
        print(numbers)
    for j in journey:
        print(j)
    return min(numbers)


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
