from collections import defaultdict


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def get_groups(stream):

    i = 0
    leng = len(stream)
    garbage_mode = False
    skip_next = False
    gcol = 0
    gcan = 0

    final = ''
    while i < leng:
        char = stream[i]
        if garbage_mode and char == '>':
            garbage_mode = False
        elif char == '!':
            i += 1
        elif garbage_mode:
            gcol += 1
            pass
        elif char in ['{', '}']:
            final += char
        elif char == '<':
            garbage_mode = True

        i += 1
    print(gcol)
    return final


def get_score(groups):
    depth = 0
    score = 0
    for char in groups:
        if char == '{':
            depth += 1
        elif char == '}':
            score += depth
            depth -= 1
    return score


def part1(data):
    for line in data:
        groups = get_groups(line)
        score = get_score(groups)
    return score


def part2(data):
    for line in data:
        print(line)
        groups = get_groups(line)
    return 2


def test():
    data = load_data("test_input.txt")
    part1(data)
    part2(data)


if __name__ == "__main__":
    test()
    data = load_data("input.txt")
    part1(data)