from copy import deepcopy

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

def prep_data(data):
    notes = []
    display = []
    for line in data:
        n, d = line.split(' | ')
        notes.append([''.join(sorted(_n)) for _n in n.split(' ')])
        display.append([''.join(sorted(_d)) for _d in d.split(' ')])
    return notes, display


def part1(data):
    display_count = [[len(_n) for _n in line.split(' | ')[1].split(' ')] for line in data]
    return sum([count in [2, 4, 3, 7] for signal_count in display_count for count in signal_count])


count_dict = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}


def get_value(note, display):
    number_options = {i: list([j for j in note if i in count_dict[len(j)]]) for i in range(10)}
    results = {i: number_options[i][0] for i in [1, 4, 7, 8]}

    # Retrieve values
    for option in number_options[6]:
        all_1 = all([c in option for c in results[1]])
        if all_1:
            if all([c in option for c in results[4]]):
                x = 9
            else:
                x = 0
        else:
            x = 6
        results[x] = option

    for option in number_options[5]:
        all_1 = all([c in option for c in results[1]])
        if all_1:
            x = 3
        elif not all_1 and sum([c in option for c in results[6]]) == 4:
            x = 2
        else:
            x = 5
        results[x] = option

    _results = {j: str(i) for i, j in results.items()}

    return int(''.join([_results[_d] for _d in display]))


def part2(data):
    notes, displays = prep_data(data)
    return sum([get_value(note, display) for note, display in zip(notes, displays)])


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=0, a2=5353)
    test(file_name='day8b.txt', part1=part1, part2=part2, a1=26, a2=61229)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
