from functions.generic import *
from functions.load_data import load_data, load_data_split_empty
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


# import re
# result = re.findall(r'[-+]?\d*(?:.\d+)?', "hello 42 I'm a -32 string 30")
# print(result)

def prep_data(data):
    results = []
    for block in data:
        results.append([eval(block[0]), eval(block[1])])
    return results


def compare(packet1, packet2, index=0, depth=0):
    print("Compare", packet1, packet2)
    _out = None
    while True:
        if not packet2 and packet1:
            print("Right is empty left isn't - False")
            return False
        elif not packet1 and not packet2:
            print("Compare", packet1, packet2)
            print("Both empty - continue")
            return True
        elif not packet1 and packet2:
            print("Left is empty right isn't - True")
            return True

        elif type(packet1[index]) == int and type(packet2[index]) == int:
            if packet1[index] > packet2[index]:
                print("1 bigger than 2 - False")
                return False
            elif packet1[index] < packet2[index]:
                print("Left smaller than right - True")
                return True
            else:
                print("Left & right equal - continue")
        elif type(packet1[index]) == list and type(packet2[index]) == list:
            print("Nested lists")
            _out = compare(packet1[index], packet2[index], 0, depth + 1)
        elif type(packet1[index]) == int and type(packet2[index]) == list:
            print("int vs list")
            _out = compare([packet1[index]], packet2[index], 0, depth + 1)
        elif type(packet1[index]) == list and type(packet2[index]) == int:
            print("list vs int")
            _out = compare(packet1[index], [packet2[index]], 0, depth + 1)

        index += 1
        if _out is False:
            return False
        elif _out is True and depth == 0:
            return _out
        elif _out is True:
            break

        if len(packet1) == index or len(packet2) == index:
            if len(packet1) == len(packet2):
                print('Left values same length as right')
                _out = True
            elif len(packet1) < len(packet2):
                print('Left ran out of values first - continue')
                _out = True
            else:
                print('Right ran out of values first - False')
                return False

        if _out is True and depth == 0:
            return _out
        elif _out is True:
            break
    if depth == 0:
        print("True for", packet1, '-', packet2)
        return True


def compare_sets(data):
    count = 0
    for j, (packet1, packet2) in enumerate(data, start=1):
        print('----- next -----')
        if compare(packet1, packet2):
            print(j, 'true', packet1, packet2)
            count += j
    return count


def part1(data):
    data = prep_data(data)
    return compare_sets(data)


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=13, a2=2, _load_data=load_data_split_empty)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split_empty(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
