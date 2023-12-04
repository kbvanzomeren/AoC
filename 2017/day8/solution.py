from collections import defaultdict


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    results = defaultdict(lambda: 0)
    maxy = 0
    for line in data:
        var, option, value, _, var2, sign, value2 = line.split(' ')

        if eval(f"{results[var2]} {sign} {value2}"):
            _option = -1 if option == 'dec' else 1
            results[var] += _option * int(value)

        _max = max([value for _, value in results.items()])
        if _max > maxy:
            maxy = _max

    print(max([value for _, value in results.items()]))
    print(maxy)

    return data


def part1(data):
    return 5


def part2(data):
    return 2


def test():
    data = load_data("test_input.txt")


if __name__ == "__main__":
    test()
    data = load_data("input.txt")
