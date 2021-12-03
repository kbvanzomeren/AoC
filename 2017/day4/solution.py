
def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    data = [line.split(' ') for line in _data]
    return data


def part1(data):
    valid = 0
    for password in data:
        if len(password) == len(set(password)):
            valid += 1
    return valid


def part2(data):
    valid = 0
    for password in data:
        if len(password) == len(set(password)):
            sorted_words = [''.join(sorted(word)) for word in password]
            print(sorted_words)
            if len(password) == len(set(sorted_words)):
                valid += 1
    return valid


def test() -> None:
    data = load_data("test_input.txt")
    # assert part1(data) == 2
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
