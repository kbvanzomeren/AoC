
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def part1(data):
    ans = []
    for line in data:
        _sum = 0
        for x1, x2 in zip(line, line[1:] + line[0]):
            if x1 == x2:
                _sum += int(x1)
        ans.append(_sum)
    return ans


def part2(data):
    line = data[0]
    _sum = 0
    for x1, x2 in zip(line, line[int(len(line)/2):] + line[:int(len(line)/2)]):
        if x1 == x2:
            _sum += int(x1)

    return _sum


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == [3, 4, 0, 9]
    data = ['123123']
    assert part2(data) == 12


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
