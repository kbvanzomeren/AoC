from collections import defaultdict
from copy import deepcopy

def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return [int(x) for x in data]


def part1(data):
    current = 0
    n_adp = len(data)
    _counter = {1: 0, 2: 0, 3: 0}

    for _ in range(n_adp):
        _min = min(data)
        diff = _min - current
        _counter[diff] += 1
        data.remove(_min)
        current = _min

    _counter[3] += 1
    return _counter[1] * _counter[3]


def part2a(data):
    current = 0
    n_adp = len(data)
    data = sorted(data)
    # data.reverse()

    computed = {x: 0 for x in data}

    for i, _max in enumerate(data):
        options = len([x for x in data[i + 1: i + 4] if x < _max + 4])
        computed[_max] = options



    computed[max(data)] = 1
    ans = 1
    for _, value in computed.items():
        ans *= value

    print(computed)
    print(ans)
    return ans


def part2b(data):
    options = [[1]]
    _continue = True
    data = sorted(data)
    _max = max(data)
    # data.append(_max + 3)

    while any(option[-1] != _max for option in options):
        for option in options:
            val = option[-1]
            _in = data.index(val)
            nop = [x for x in data[_in + 1: _in + 4] if x < val + 4]

            if not nop:
                pass
            elif len(nop) == 1:
                option.append(nop[0])
            else:
                for nval in nop[1:]:
                    nlst = list(option)
                    nlst.append(nval)
                    options.append(nlst)
                option.append(nop[0])
            # print('Start')
            # for option in options:
            #     print(option)

    # for option in options:
    #     print(option)


    print([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49] in options)
    print([3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45, 47, 49] in options)
    print([1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49] in options)
    print(len(options))
    return len(options)


def get_options(device, data, jol=0):
    if jol == device:
        return 1
    if jol > device:
        return 0
    options = 0
    # next_pos = [x for x in data[pos + 1: pos + 4] if x < data[pos] + 4]

    for step in range(1, 4):
        if jol + step in data:
            options += get_options(device, data, jol + step)

    return options


def part2(data):
    _continue = True
    data.sort()
    device = max(data) + 3
    data.append(device)
    return get_options(device, data)


def part2aa(data):

    data.sort()
    device = max(data) + 3
    data2 = list(data)
    data2.append(device)
    sub_solutions = [x for x in data if x + 1 not in data and x + 2 not in data]
    ss_options = 1
    for jol, end in zip([0] + sub_solutions, sub_solutions + [device]):
        ss_options *= get_options(end, data2, jol)

    print(ss_options)
    return ss_options

def test():
    data = load_data("test_input.txt")
    assert part1(list(data)) == 35
    assert part2aa(list(data)) == 8

    data = load_data("test_input2.txt")
    assert part1(list(data)) == 220
    assert part2aa(list(data)) == 19208


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(list(data))}")
    print(f"Answer to part 2 is {part2aa(list(data))}")
