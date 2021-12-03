from collections import Counter


def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()
    return [route.split(',') for route in _data]


def part1(data):

    for route in data:
        mydict = {
            'ne': 0,
            'n': 0,
            'nw': 0,
            'se': 0,
            's': 0,
            'sw': 0,
        }
        for key, value in Counter(route).items():
            mydict[key] = value

        for i, j in zip(['ne', 'n', 'nw'], ['sw', 's', 'se']):
            if mydict[i] != 0 and mydict[j] != 0:
                _store = min(mydict[i], mydict[j])
                mydict[i] -= _store
                mydict[j] -= _store

        for i, j, k in zip(['ne', 'se', 'ne', 'nw', 'se', 'sw'], ['nw', 'sw', 's', 's', 'n', 'n'], ['n', 's', 'se', 'sw', 'ne', 'nw']):
            if mydict[i] != 0 and mydict[j] != 0:
                _store = min([mydict[i], mydict[j]])
                mydict[i] -= _store
                mydict[j] -= _store
                mydict[k] += _store

        result = {key: value for key, value in mydict.items() if value != 0}
        print(sum([value for _, value in result.items()]))

    return 1


def part2(data):
    mydict = {
        'ne': 0,
        'n': 0,
        'nw': 0,
        'se': 0,
        's': 0,
        'sw': 0,
    }

    route = data[0]
    _max = 0

    for i in range(700, len(route)):
        current_route = route[:i]

        for key, value in Counter(current_route).items():
            mydict[key] = value

        for i, j in zip(['ne', 'n', 'nw'], ['sw', 's', 'se']):
            if mydict[i] != 0 and mydict[j] != 0:
                _store = min(mydict[i], mydict[j])
                mydict[i] -= _store
                mydict[j] -= _store

        for i, j, k in zip(['ne', 'se', 'ne', 'nw', 'se', 'sw'], ['nw', 'sw', 's', 's', 'n', 'n'], ['n', 's', 'se', 'sw', 'ne', 'nw']):
            if mydict[i] != 0 and mydict[j] != 0:
                _store = min([mydict[i], mydict[j]])
                mydict[i] -= _store
                mydict[j] -= _store
                mydict[k] += _store

        result = {key: value for key, value in mydict.items() if value != 0}
        _l = sum([value for _, value in result.items()])
        if _l > _max:
            _max = _l

    print(_max)
    return 2


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 1
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
