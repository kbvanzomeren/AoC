from functools import lru_cache

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def split_data(data, part=1):
    result = []
    for line in data:
        spring, groups = line.split(' ')
        groups = tuple(int(g) for g in groups.split(','))
        if part == 1:
            result.append((spring, groups))
        else:
            result.append(('?'.join([spring for _ in range(5)]), groups * 5))
    return result


@lru_cache
def get_spring_positions(springs, groups):
    if not groups:
        return '#' not in springs

    if groups and not springs:
        return 0

    group = groups[0]
    groups = groups[1:]
    group_remainder = sum(groups) + len(groups) - 1
    count = 0
    for i in range(len(springs) - group_remainder - group):
        current_spring = '.' * i + '#' * group + '.'
        if all(j == '#' and k in ["#", "?"] or j == '.' and k in ['.', '?']
               for j, k in zip(current_spring, springs[:i + group + 1])):
                    count += get_spring_positions(springs[i + group + 1:].lstrip('.'), groups)
    return count


def part1(data):
    springs = split_data(data)
    count = 0
    for spring, groups in springs:
        count += get_spring_positions(spring.lstrip('.'), groups)
    return count


def part2(data):
    springs = split_data(data, part=2)
    count = 0
    for spring, groups in springs:
        count += get_spring_positions(spring.lstrip('.'), groups)
    return count


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
