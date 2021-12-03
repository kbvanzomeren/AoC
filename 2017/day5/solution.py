
def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    data = [int(x) for x in _data]
    return data


def part1(data):
    steps = 0
    postion = 0
    while 0 <= postion < len(data):
        old_postion = postion
        postion += data[postion]
        data[old_postion] += 1
        steps += 1
    return steps


def part2(data):

    steps = 0
    postion = 0
    while 0 <= postion < len(data):
        old_postion = postion
        postion += data[postion]
        if data[old_postion] >= 3:
            data[old_postion] -= 1
        else:
            data[old_postion] += 1
        steps += 1
    return steps


def test() -> None:
    data = load_data("test_input.txt")
    # assert part1(data) == 5
    assert part2(data) == 10


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
