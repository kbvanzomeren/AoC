from functions.generic import *
from functions.load_data import load_data, load_data_split_empty
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data, part=1):
    results = []
    for block in data:
        if part == 1:
            results.append([eval(block[0]), eval(block[1])])  # ☠︎
        else:
            results.append(eval((block[0])))  # ☠︎
            results.append(eval((block[1])))  # ☠︎
    return results


def compare(packet1, packet2):
    type1, type2 = type(packet1), type(packet2)
    if type1 == int and type2 == int:
        if packet1 == packet2:
            return None
        return packet1 < packet2

    if type1 == list and type2 == list:
        for sub_packet1, sub_packet2 in zip(packet1, packet2):
            result = compare(sub_packet1, sub_packet2)
            if result is not None:
                return result
        if len(packet1) == len(packet2):
            return None
        return len(packet1) < len(packet2)

    if type1 == int:
        return compare([packet1], packet2)
    return compare(packet1, [packet2])


def part1(data):
    data = prep_data(data)
    count = 0
    for j, (packet1, packet2) in enumerate(data, start=1):
        if compare(packet1, packet2):
            count += j
    return count


def part2(data):
    packages = prep_data(data, part=2)
    result = 1
    dividers = [[[2]], [[6]]]
    for divider in dividers:
        result *= sum(1 for package in packages + dividers if compare(package, divider)) + 1
    return result


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=13, a2=140, _load_data=load_data_split_empty)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split_empty(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
