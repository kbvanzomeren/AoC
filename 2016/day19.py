# from functions.load_data import load_data
import collections

from functions.generic import *
from functions.load_data import load_data
from functions.test import test
from collections import deque

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')

def part1(data):
    n_elves = 5
    elves = list(range(1, n_elves + 1, 1))
    while True:
        is_uneven = False
        if len(elves) % 2:
            is_uneven = True
        elves = [elf for i, elf in enumerate(elves) if (i + 1) % 2]
        if is_uneven:
            elves.pop(0)
        if len(elves) == 1:
            return elves[0]
    return 1


ELF_COUNT = 3014603
def part2quick(dat):
    left = collections.deque()
    right = collections.deque()
    for i in range(1, ELF_COUNT+1):
        if i < (ELF_COUNT // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]

def part2(data):
    n_elves = ELF_COUNT
    elves = list(range(1, n_elves + 1, 1))

    ind = 0
    while True:
        removed_ind = (ind + n_elves // 2) % n_elves
        elves.pop(removed_ind)
        n_elves -= 1
        if ind == n_elves:
            ind %= n_elves
        elif removed_ind < ind:
            pass
        else:
            ind += 1
        if n_elves == 1:
            break

    result = [e for e in elves if e]
    return result[0]


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
    print(f"Answer to part 2 is {part2b(data)}")