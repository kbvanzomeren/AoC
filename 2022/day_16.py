from copy import copy

from functions.generic import *
from functions.load_data import load_data


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
    def __init__(self, current, last, opened, rp, ovv, n_opened):
        self.rp = rp
        self.ovv = ovv
        self.opened = opened
        self.n_opened = n_opened
        self.current = current
        self.last = last

    def __str__(self):
        return f"{'-'.join(sorted(self.current))}_{'-'.join(sorted(self.opened))}"


def clean_dataset(states, minute, max_ovv, _time=26):
    remaining = (_time - minute)
    max_states = max([s.rp + remaining * s.ovv for s in states])
    max_points = remaining * max_ovv
    if max_points >= max_states:
        return states
    return [s for s in states if s.rp + max_points >= max_states]


def run(data, runtime=30):
    minutes = 1
    volcanos = [Volcano(('AA', 'AA'), (None, None), set(), 0, 0, 0)]
    visited_val = {}
    visited = set()
    max_open = sum(x[0] > 0 for _, x in data.items())
    max_ovv = sum(x[0] for _, x in data.items())
    while minutes < runtime:
        new_volcanos = []
        for volcano in volcanos:
            volcano.rp += volcano.ovv
            if volcano.n_opened == max_open:
                new_volcanos.append(volcano)
                continue
            for room in data[volcano.current[0]][1]:
                for room2 in data[volcano.current[1]][1]:
                    if room != volcano.last[0] and room2 != volcano.last[1]:
                        new_volcanos.append(Volcano((room, room2), volcano.current, copy(volcano.opened), volcano.rp, volcano.ovv, volcano.n_opened))
            if volcano.current[0] not in volcano.opened and data[volcano.current[0]][0] and volcano.current[1] not in volcano.opened and data[volcano.current[1]][0] and volcano.current[0] != volcano.current[1]:
                opened = copy(volcano.opened)
                opened.add(volcano.current[0])
                for room2 in data[volcano.current[1]][1]:
                    new_volcanos.append(
                        Volcano((volcano.current[0], room2), ('None', volcano.current[1]), opened, volcano.rp, volcano.ovv + data[volcano.current[0]][0], volcano.n_opened + 1))
                opened = copy(volcano.opened)
                opened.add(volcano.current[1])
                for room in data[volcano.current[0]][1]:
                    new_volcanos.append(
                        Volcano((room, volcano.current[1]), (volcano.current[0], 'None'),  opened, volcano.rp, volcano.ovv + data[volcano.current[1]][0], volcano.n_opened + 1))
                opened = copy(volcano.opened)
                opened.add(volcano.current[1])
                opened.add(volcano.current[0])
                new_volcanos.append(
                    Volcano((volcano.current[0], volcano.current[1]), (None, 'None'),  opened, volcano.rp, volcano.ovv + data[volcano.current[0]][0] + data[volcano.current[1]][0], volcano.n_opened + 2))
            elif volcano.current[0] not in volcano.opened and data[volcano.current[0]][0]:
                opened = copy(volcano.opened)
                opened.add(volcano.current[0])
                for room2 in data[volcano.current[1]][1]:
                    new_volcanos.append(
                        Volcano((volcano.current[0], room2), ('None', volcano.current[1]), opened, volcano.rp, volcano.ovv + data[volcano.current[0]][0], volcano.n_opened + 1))
            elif volcano.current[1] not in volcano.opened and data[volcano.current[1]][0] and volcano.current[0] != volcano.current[1]:
                opened = copy(volcano.opened)
                opened.add(volcano.current[1])
                for room in data[volcano.current[0]][1]:
                    new_volcanos.append(
                        Volcano((room, volcano.current[1]), (volcano.current[0], 'None'),  opened, volcano.rp, volcano.ovv + data[volcano.current[1]][0], volcano.n_opened + 1))

        volcanos = []
        # print(len(new_volcanos))
        new_volcanos = clean_dataset(new_volcanos, minutes, max_ovv, runtime)

        for nv in new_volcanos:
            _nv = str(nv)
            if _nv in visited:
                if nv.rp > visited_val[_nv]:
                    visited_val[_nv] = nv.rp
                    volcanos.append(nv)
            else:
                visited_val[_nv] = nv.rp
                visited.add(_nv)
                volcanos.append(nv)
        # print(len(volcanos))
        minutes += 1
    _max = 0
    for v in volcanos:
        if v.rp > _max:
            _max = v.rp
    return _max


def part1(data):
    result = prep_data(data)
    return run(result, 31)


def part2(data):
    result = prep_data(data)
    return run(result, 27)


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1651, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
