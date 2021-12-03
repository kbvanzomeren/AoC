import itertools


def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    return [int(n) for n in _data]


def part1(data, n=5):
    length = len(data)
    for i in range(n, length):
        if data[i] not in [sum(pair) for pair in itertools.combinations(data[i - n: i], 2)]:
            ans = data[i]
    return ans


def part2(data, n):
    goal = part1(data, n)
    goal_not_found = True
    check_combo = 2
    length = len(data)

    while goal_not_found:
        _list = [sum(data[i: i + check_combo]) for i in range(length - check_combo)]
        if goal in _list:
            index = _list.index(goal)
            ans = [data[i: i + check_combo] for i in range(length - check_combo)][index]
            goal_not_found = False
        check_combo += 1

    return min(ans) + max(ans)


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data, 5) == 127
    assert part2(data, 5) == 62


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data, 25)}")
    print(f"Answer to part 2 is {part2(data, 25)}")
