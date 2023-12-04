from collections import defaultdict

def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    results = []
    slots = []
    for line in data:
        if 'mask = ' in line:
            if slots:
                results.append([mask, slots])
                slots = []
            mask = line.split(' = ')[-1]

        else:
            val1, val2 = line.split(' = ')
            bit = "{0:b}".format(int(val2))
            val3 = '0' * (36-len(bit)) + bit
            slots.append([val1.split('[')[-1][:-1], val3])
    if slots:
        results.append([mask, slots])
    return results


def part1(data):
    data.reverse()
    ans = {}
    for mask, slots in data:
        slots.reverse()
        for i, bit in slots:
            if i not in ans:
                ans[i] = ''
                for j, _b in enumerate(bit):
                    ans[i] += _b if mask[j] == 'X' else mask[j]

    _ans = 0
    for _, _bit in ans.items():
        _ans += int(_bit, 2)

    return _ans


def part2(data):
    ans = {}
    for mask, slots in data:
        for i, bit in slots:
            __bit = "{0:b}".format(int(i))
            _bit = '0' * (36 - len(__bit)) + __bit
            result = ''
            for j, _b in enumerate(_bit):
                result += _b if mask[j] == '0' else mask[j]

            # print(_bit)
            # print(mask)
            # print(result)

            masks = [result]
            while any(['X' in _mask for _mask in masks]):
                _masks2 = []
                for _mask in masks:
                    _num = _mask.index('X')
                    val1 = _mask[:_num] + '0' + _mask[_num + 1:]
                    val2 = _mask[:_num] + '1' + _mask[_num + 1:]
                    _masks2.append(val1)
                    _masks2.append(val2)

                masks = _masks2
            addr = [int(xx, 2) for xx in _masks2]

            b_value = ''
            for j, _b in enumerate(_bit):
                b_value += _b if mask[j] == 'X' else mask[j]

            for ind in addr:
                ans[ind] = bit

    _ans = 0
    for _, _bit in ans.items():
        _ans += int(_bit, 2)
    return _ans


def test():
    data = load_data("test_input.txt")
    assert part1(data) == 165
    data = load_data("test_input2.txt")
    assert part2(data) == 208


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    # print(f"Answer to part 1 is {part1(data)}")
    print(part2(data))
