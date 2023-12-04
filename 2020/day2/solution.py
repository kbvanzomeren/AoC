
def load_data(file):
    data = []
    with open(file, "r") as fd:
        for line in fd.readlines():
            _bounds, _letter, _pass = line.split(' ')
            _lower, _higher = _bounds.split('-')
            data.append([int(_lower), int(_higher), _letter.strip(':'), _pass])
    return data


def part1(data):
    valid = 0
    for [lower, higher, letter, password] in data:
        _c = password.count(letter)
        if lower <= _c <= higher:
            valid += 1
    return valid


def part2(data):
    valid = 0
    for [lower, higher, letter, password] in data:
        if password[lower - 1] == letter and password[higher - 1] == letter:
            pass
        elif password[lower - 1] == letter:
            valid += 1

        elif password[higher - 1] == letter:
            valid += 1
    return valid


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 2
    assert part2(data) == 1


if __name__ == "__main__":
    test()

    input_data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(input_data)}")
    print(f"Answer to part 1 is {part2(input_data)}")
