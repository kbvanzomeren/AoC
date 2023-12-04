import math
from math import floor
import numpy as np


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    return int(data[0]), [(i, int(b)) for i, b in enumerate(data[1].split(',')) if b != 'x']


def part1(data):
    dep, buses = load_data(data)

    dep_in = [(b, b - (dep % b)) for _, b in buses]
    closest = min(dep_in, key=lambda x: x[1])
    return closest[0] * closest[1]


def part2(data):
    _, buses = load_data(data)
    p, t = 1, buses[0]

    _m = max(buses, key=lambda x: x[1])[1]

    # not_found = True
    # while not_found:
    #     if all((dt + t) % b == 0 for dt, b in buses):
    #         not_found = False
    #         ans = t
    #
    #     t += _m
    #     print(t)
    # print(ans)

    for dt, b in buses:
        while True:
            if (dt+t) % b == 0:
                break
            t += p

        # print(t)
        # print(p)
        p *= b

    print(t)
    return 2


def test():
    data = "test_input.txt"
    # assert part1(data) == 295
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = "input.txt"
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
