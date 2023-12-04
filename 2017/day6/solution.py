
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().split('\t')
    return [int(x) for x in data]


def part1(data):
    visted = []
    position = data.index(max(data))
    len_data = len(data)
    step = 0
    while data not in visted:

        visted.append(list(data))
        value = data[position]
        data[position] = 0
        for i in range(value):
            data[(position + i + 1) % len_data] += 1
        position = data.index(max(data))
        step += 1
    print(step - visted.index(data))

    return step


def part2(data):
    return 2


def test():
    _data = load_data("test_input.txt")
    data = list(_data)
    assert part1(data) == 5
    data = list(_data)
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    _data = load_data("input.txt")
    data = list(_data)
    print(f"Answer to part 1 is {part1(data)}")
    data = list(_data)
    print(f"Answer to part 2 is {part2(data)}")
