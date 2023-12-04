# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def create_next_row(row):
    temp_row = '.' + row + '.'
    new_row = ''
    chunks = [temp_row[i:i+3] for i in range(len(temp_row) - 2)]
    for chunk in chunks:
        if chunk in ['^^.', '.^^', '^..', '..^']:
            new_row += '^'
        else:
            new_row += '.'
    return new_row


def gen_map(row, size=3):
    final_map = [row]
    for i in range(size - 1):
        row = create_next_row(row)
        final_map.append(row)

    # for row in final_map:
    #     print(row)
    return final_map


def part1(data):
    size, row = data[0].split(',')
    _map = gen_map(row, int(size))
    return ''.join(_map).count('.')


def part2(data):
    size, row = data[0].split(',')
    _map = gen_map(row, int(size) * 10000)
    return ''.join(_map).count('.')


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=38, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")