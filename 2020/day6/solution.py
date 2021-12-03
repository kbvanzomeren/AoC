
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    if data[-1] != '':
        data.append('')
    return data


def part1(data):
    ans = ''
    all_ans = []
    for line in data:
        if line:
            ans += line
        else:
            all_ans.append(''.join(set(ans)))
            ans = ''
    return sum([len(_a) for _a in all_ans])


def part2(data):
    counts = 0
    ans = ''
    group_ans = []
    for line in data:
        if line:
            ans += line
            group_ans.append(line)
        else:
            unique = ''.join(set(ans))
            for _c in unique:
                if all([_a.count(_c) for _a in group_ans]):
                    counts += 1
            ans = ''
            group_ans = []

    return counts


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 11
    assert part2(data) == 6


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
