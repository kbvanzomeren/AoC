from collections import defaultdict
import re


def load_data(file):
    with open(file, "r") as fd:
        data = {}
        for line in fd.read().splitlines():
            ind, l = re.findall(r'\d+', line)
            data[int(ind)] = int(l)

    result = {}
    for i in range(max(data) + 1):
        result[i] = data.get(i, 0)
    return result


def run(data, wait=0, calc_punish=True):
    punish = 0
    for layer, depth in data.items():
        timy = layer + wait
        if depth and not timy % ((depth - 1) * 2):
            if calc_punish:
                punish += layer * depth
            else:
                return -1

    return punish


def part1(data):
    return run(data)


def part2(data):
    time = 0
    while True:
        result = run(data, time, calc_punish=False)
        if result == 0:
            return time
        time += 1


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 24
    assert part2(data) == 10


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
