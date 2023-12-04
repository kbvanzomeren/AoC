from collections import defaultdict
from copy import copy
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    start = data[0]
    rules = {}
    for rule in data[2:]:
        x1, x2, = rule.split(' -> ')
        rules[x1] = [x1[0] + x2, x2 + x1[1], x2]
    return start, rules


def get_template(template, rules, steps=10):
    pairs = [i + j for i, j in zip(template[:-1], template[1:])]
    counts = defaultdict(int)

    for pair in pairs:
        counts[pair] += 1

    results = defaultdict(int)
    for c in template:
        results[c] += 1

    for i in range(steps):
        new_counts = defaultdict(int)
        for pair, n in counts.items():
            p1, p2, r = rules[pair]
            new_counts[p1] += n
            new_counts[p2] += n
            results[r] += n
        counts = copy(new_counts)

    results_sort = sorted(results.values())
    return results_sort[-1] - results_sort[0]


def part1(data):
    template, rules = prep_data(data)
    return get_template(template, rules, steps=10)


def part2(data, steps=40):
    template, rules = prep_data(data)
    return get_template(template, rules, steps=steps)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1588, a2=2188189693529)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data, 40)}")
