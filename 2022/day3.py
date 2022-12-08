import string

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep
import string

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

all_score = {c: i for i, c in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1)}


def part1(data):
    score = 0
    for line in data:
        l = len(line)
        c1, c2 = set(line[:l//2]), set(line[l//2:])
        score += sum([all_score[letter] for letter in c1 if letter in c2])
    return score


def part2(data):
    score = 0
    for i in range(len(data)//3):
        elf1, elf2, elf3 = data[i * 3: i * 3 + 3]
        for letter in elf1:
            if letter in elf2 and letter in elf3:
                score += all_score[letter]
                break
    return score


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=157, a2=70)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
