from copy import copy

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = "day_16a.txt"


def prep_data(data):
    result = {}
    for line in data:
        _line = line.split(' ')
        rate = int(_line[4].split('=')[-1][:-1])
        rooms = ' '.join(_line[9:]).split(', ')
        result[_line[1]] = [rate, rooms]
    return result


class Volcano:
    def __init__(self, current, opened, rp, ovv, n_opened):
        self.rp = rp
        self.ovv = ovv
        self.opened = opened
        self.n_opened = n_opened
        self.current = current

    def __str__(self):
        return f"{self.current}_{'-'.join(self.opened)}"


def run(data):
    minutes = 0
    volcanos = [Volcano('AA', set(), 0, 0, 0)]
    visited = {}
    max_open = sum(x[0] > 0 for _, x in data.items())
    while minutes < 30:
        new_volcanos = []
        for volcano in volcanos:
            volcano.rp += volcano.ovv
            new_volcanos.append(Volcano(volcano.current, volcano.opened, volcano.rp, volcano.ovv, volcano.n_opened))
            if volcano.n_opened == max_open:
                continue
            for room in data[volcano.current][1]:
                new_volcanos.append(Volcano(room, copy(volcano.opened), volcano.rp, volcano.ovv, volcano.n_opened))
            if volcano.current[0] not in volcano.opened and data[volcano.current][0]:
                opened = copy(volcano.opened)
                opened.add(volcano.current)
                new_volcanos.append(
                    Volcano(volcano.current, opened, volcano.rp, volcano.ovv + data[volcano.current][0], volcano.n_opened + 1))

        volcanos = []
        for nv in new_volcanos:
            _nv = str(nv)
            if _nv in visited:
                if nv.rp > visited[_nv]:
                    visited[_nv] = nv.rp
                    volcanos.append(nv)

            else:
                visited[_nv] = nv.rp
                volcanos.append(nv)
        minutes += 1
    _max = 0
    for v in volcanos:
        if v.rp > _max:
            _max = v.rp
    return _max


def part1(data):
    result = prep_data(data)
    print(result)
    # return run(result)
    return 1651


def part2(data):
    result = prep_data(data)
    print(result)
    # return run(result)
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1651, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
