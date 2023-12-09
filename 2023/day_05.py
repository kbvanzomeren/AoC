import time
from copy import deepcopy

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def parse_data(data, part=1):
    results = []
    seeds = [int(s) for s in data[0].split(': ')[1].split(' ')]
    seeds_min_max = [(seed, seed) for seed in seeds]
    if part == 2:
        seeds_min_max = [(seeds[(i * 2)], seeds[(i * 2)] + seeds[(i * 2) + 1]) for i in range(len(seeds)//2)]

    current_mapping = []
    for line in data[2:]:
        if "map" in line and "seed-to" not in line:
            results.append(list(current_mapping))
            current_mapping = []
        elif "-to-" not in line and line != '':
            des, source, _range = [int(n) for n in line.split(' ')]
            current_mapping.append([(source, source + _range), (des)])
    results.append(list(current_mapping))
    return seeds_min_max, results,


def run_rounds(seeds_min_max, _rounds):
    for j, _round in enumerate(_rounds):
        new_ranges = []
        for (seeds_min, seed_max) in seeds_min_max:
            while True:
                has_changed = False
                is_done = False
                for ((_min, _max), des) in _round:
                    # full range in option
                    if _min <= seeds_min < _max and seed_max < _max:
                        new_ranges.append((seeds_min - _min + des, seed_max - _min + des))
                        has_changed = True
                        is_done = True
                        break
                    # first part in option
                    elif _min <= seeds_min < _max:
                        new_ranges.append((seeds_min - _min + des, _max - _min + des))
                        seeds_min = _max
                        has_changed = True
                    # last part in option
                    elif _min <= seed_max < _max:
                        new_ranges.append((des, seed_max - _min + des))
                        seed_max = _min - 1
                        has_changed = True

                # Keep current range
                if not has_changed:
                    new_ranges.append((seeds_min, seed_max))
                    break

                if is_done or seeds_min == seed_max:
                    break
        seeds_min_max = deepcopy(new_ranges)
    return min([x[0] for x in seeds_min_max])


def part1(data):
    seeds_min_max, _rounds = parse_data(data)
    return run_rounds(seeds_min_max, _rounds)


def part2(data):
    seeds_min_max, _rounds = parse_data(data, part=2)
    return run_rounds(seeds_min_max, _rounds)


if __name__ == "__main__":
    start = time.time()
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=35, a2=46)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
    print("Finished after", f"{round((time.time() - start), 5)} seconds")
