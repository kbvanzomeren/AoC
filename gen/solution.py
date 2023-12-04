
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def part1(data):
    return 1


def part2(data):
    return 2


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 1
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
