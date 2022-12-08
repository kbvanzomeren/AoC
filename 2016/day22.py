# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

def prep_data(data):
    results = [[] for _ in range(31)]
    results1 = []
    ind = 0
    ii = 0
    for line in data[2:]:
        x = re.findall('[0-9]+', line)
        x = [int(i) for i in x]
        results[ind].append([[x[0], x[1]], x[2], x[3], x[4], x[5]])
        results1.append([[x[0], x[1]], x[2], x[3], x[4], x[5]])
        if x[3] > 100:
            print(x[0], x[1])
        if x[3] == 0:
            print("Empty")
            print(x[0], x[1])
        ind += 1
        ind %= 31
    return results1, results


def part1(data):
    results, _ = prep_data(data)
    pairs = 0
    for i, line in enumerate(results):
        used = line[2]
        for j, pair_line in enumerate(results):
            if i == j:
                pass
            elif used and used <= pair_line[3]:
                pairs += 1
    return pairs



def print_map(data):
    _, data = prep_data(data)
    for i, row in enumerate(data):
        rowy = []
        for j, val in enumerate(row):
            if not i and not j:
                c = "A"
            elif not i and j == 33:
                c = "B"
            elif val[2] == 0:
                c = "E"
            elif val[2] > 100:
                c = "#"
            else:
                c = "."
            rowy.append(c)
        print(''.join(rowy))


def part2(data):
    print_map(data)
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")