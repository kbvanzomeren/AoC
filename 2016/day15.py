# from functions.load_data import load_data
from time import sleep

from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import re

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    disks = []
    for line in data:
        # print(line)
        _, positions, _, current = re.findall(r'\d+', line)
        disks.append([int(positions), int(current)])
    return disks


def run(disks, t0=0, td=0):
    while True:
        # sleep(1)
        t = t0
        success = True
        # print(t)
        for i, disk in enumerate(disks):
            t += 1
            # print()
            if (disk[1] + t) % disk[0]:
                # print("Fails on disk", i)
                success = False

        if success:
            return t0
        t0 += td





def part1(data):

    disks = prep_data(data)
    p, c = disks[0]
    t_intial = p - c - 1
    td = p
    t_release = run(disks, t_intial, td)
    return t_release


def part2(data):
    disks = prep_data(data)
    disks.append([11, 0])
    p, c = disks[0]
    t_intial = p - c - 1
    td = p
    t_release = run(disks, t_intial, td)
    return t_release


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=5, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")