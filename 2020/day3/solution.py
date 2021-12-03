
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def get_n_trees(data, dx, dy):
    trees = 0
    x = 0
    width = len(data[0])
    height = len(data)
    for y in range(0, height, dy):
        if data[y][x % width] == '#':
            trees += 1
        x += dx
    return trees


def part1(data):
    return get_n_trees(data, 3, 1)


def part2(data):
    ans = 1
    for dx, dy in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        trees = get_n_trees(data, dx, dy)
        ans *= trees
    return ans


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 7
    assert part2(data) == 336


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
