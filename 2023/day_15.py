from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def calculate_score(line, score=0):
    for c in line:
        score = ((score + ord(c)) * 17) % 256
    return score


def get_configuration(lines):
    config = defaultdict(list)
    for line in lines:
        if '=' in line:
            label, lens = line.split('=')
        else:
            label = line[:-1]

        score = calculate_score(label)
        match_index = [i for i, (current, _) in enumerate(config[score]) if label == current]

        if '=' in line and match_index:
            config[score][match_index[0]] = (label, lens)
        elif '=' in line:
            config[score].append((label, lens))
        elif '-' in line and match_index:
            config[score].pop(match_index[0])
    return config


def part1(data):
    return sum(calculate_score(line) for line in data[0].split(','))


def part2(data):
    config = get_configuration(data[0].split(','))
    return sum((key + 1) * i * int(lens) for key, value in config.items() for i, (_, lens) in enumerate(value, start=1))


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
