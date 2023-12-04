from functions.generic import *
from functions.load_data import load_data

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

rep_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def transform_data(data):
    results = []
    for line in data:
        pos = {}
        for number, value in rep_num.items():
            if number in line:
                pos[line.find(number)] = value
                pos[line.rfind(number)] = value
        if pos:
            _min, _max = min(pos), max(pos)
            line = line[:_min] + str(pos[_min]) + line[_min + 1:]
            line = line[:_max] + str(pos[_max]) + line[_max + 1:]
        results.append(line)
    return results


def calibrate(data, transform=False):
    if transform:
        data = transform_data(data)
    result = 0
    for line in data:
        digits = get_digits(line)
        result += int(digits[0] + digits[-1])
    return result


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {calibrate(data)}")
    print(f"Answer to part 2 is {calibrate(data, True)}")
