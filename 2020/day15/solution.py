from collections import defaultdict
def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()

    data = [int(x) for x in _data[0].split(',')]

    return data


def part1(data, n=2021):
    last = {}
    # order = []

    for turn, number in enumerate(data):
        last[number] = turn + 1

    current = 0

    for turn in range(len(data) + 1, n):
        previous = current
        if current not in last:
            current = 0
        else:
            current = turn - last[current]
        last[previous] = turn

    return previous


def part2(data):
    return 2


def test():
    data = load_data("test_input.txt")
    assert part1(data, 2021) == 1
    # assert part1(30000000) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part1(data, 30000001)}")
