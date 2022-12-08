import re
from collections import defaultdict


def load_data(file):
    data = defaultdict(list)
    with open(file, "r") as fd:
        for line in fd.read().splitlines():
            numbers = re.findall(r'\d+', line)
            for i, n in enumerate(numbers):
                for j, ni in enumerate(numbers):
                    if i != j:
                        data[int(n)].append(int(ni))
    return data

def get_group(data, start):
    to_visit = list(data[start])
    visited = [start]
    while to_visit:
        for v in to_visit:
            visited.append(v)
            to_visit.remove(v)
            for vi in data[v]:
                if vi not in visited:
                    visited.append(vi)
                    to_visit.append(vi)
    return list(set(visited))


def part1(data):
    return len(get_group(data, 0))


def part2(data):
    visited = []
    groups = []
    for i in range(len(data)):
        if i not in visited:
            group = get_group(data, i)
            visited += group
            groups.append(group)
    for i in range(len(data)):
        if i not in visited:
            print(i)
    # print(groups)
    return len(groups)


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 6
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
