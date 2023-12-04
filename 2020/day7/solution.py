import collections


def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    data = {}
    data2 = {}
    for rule in _data:
        _rule = rule.split(',')


        if 'no other bags' in rule:
            data['-'.join(_rule[0].split(' ')[0:2])] = []
            data2['-'.join(_rule[0].split(' ')[0:2])] = 1

        else:
            bags = ['-'.join(_rule[0].split('bags contain')[-1].split(' ')[2:4])]
            bags += ['-'.join(_sub.split(' ')[2:4]) for _sub in _rule[1:]]
            data['-'.join(_rule[0].split(' ')[0:2])] = bags

            bags = ['-'.join(_rule[0].split('bags contain')[-1].split(' ')[1:2])]
            bags += ['-'.join(_sub.split(' ')[1:2]) for _sub in _rule[1:]]
            data2['-'.join(_rule[0].split(' ')[0:2])] = [int(x) for x in bags]

    return data, data2
#
# def prep_data(data):
#     return _data


def part1(data):
    has_changed = True
    while has_changed:
        has_changed = False
        for outer, inner in data.items():
            for i in inner:
                if i in data:
                    inner2 = data[i]
                    inner3 = inner + [x for x in inner2 if x not in inner]

                    if collections.Counter(inner3) != collections.Counter(inner):
                        has_changed = True
                        data[outer] = inner3

    valid = 0
    for key, values in data.items():
        if 'shiny-gold' in values:
            valid += 1

    return valid


def part2(data, data2):

    final_bag = [key for key, value in data2.items() if type(value) == int]
    has_changed = True
    while has_changed:
        has_changed = False
        for key, value in data.items():
            if key not in final_bag and all([bag in final_bag for bag in value]):
                _amount = 0
                for bag, amount in zip(value, data2[key]):
                    _amount += amount * data2[bag]

                data2[key] = _amount + 1
                has_changed = True
                final_bag = [key for key, value in data2.items() if type(value) == int]

    # print(data2['shiny-gold'])
    return data2['shiny-gold'] - 1


def test() -> None:
    data, data2 = load_data("test_input.txt")
    assert part1(data) == 4
    assert part2(data, data2) == 32

    data, data2 = load_data("test_input2.txt")
    assert part2(data, data2) == 126


if __name__ == "__main__":
    test()

    data, data2 = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data, data2)}")
