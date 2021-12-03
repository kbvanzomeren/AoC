
def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    data = [[int(_x) for _x in line.split('	')] for line in _data]
    return data


def part1(data):
    _sum = 0
    for line in data:
        _sum += max(line) - min(line)
    return _sum


def part2(data):
    _sum = 0
    for line in data:
        for _x in line:
            for _y in line:
                if _x != _y and not _x % _y:
                    _sum += _x/_y

    return _sum


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 18
    # assert part2(data) == 12


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
