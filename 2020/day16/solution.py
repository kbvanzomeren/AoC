
def load_data(file):
    with open(file, "r") as fd:
        _data = fd.read().splitlines()

    i = 0
    _all_rules = []
    _rules = {}
    _other_tickets = []
    for line in _data:
        if line == '':
            pass
        elif line == "your ticket:":
            i = 1
        elif line == "nearby tickets:":
            i = 2
        elif i == 0:
            name, sets = line.split(':')
            sets.replace(' ', '')
            _range = []
            for set in sets.split('or'):
                lower, upper = set.split('-')
                _range += range(int(lower), int(upper) + 1)
            _all_rules += _range
            _rules[name] = _range
        elif i == 1:
            _my_ticket = [int(x) for x in line.split(',')]
        else:
            _other_tickets.append([int(x) for x in line.split(',')])
    return _all_rules, _my_ticket, _other_tickets, _rules


def part1(data):
    _sum = 0
    remove = []
    for i, ticket in enumerate(data[2]):
        for n in ticket:
            if n not in data[0]:
                _sum += n
                remove.append(i)

    _remove = list(set(remove))
    _remove.sort()
    _remove.reverse()
    for i in _remove:
        data[2].pop(i)
    _options = list(data[3].keys())
    current_options = []
    for _ in range(len(data[2][0])):
        current_options += [list(_options)]

    while not all(len(x) <= 1 for x in current_options):
        for ticket in data[2]:
            for i, number in enumerate(ticket):
                for name, _range in data[3].items():
                    if name in current_options[i] and number not in _range:
                        current_options[i].remove(name)

        remove_name = []
        for option in current_options:

            if len(option) == 1:
                remove_name.append(option[0])

        for option in current_options:
            if len(option) != 1:
                for name in remove_name:
                    if name in option:
                        option.remove(name)

        # for option in current_options:
        #     print(option)

    ans = 1

    for i, name in enumerate(current_options):
        if 'departure' in name[0]:
            ans *= data[1][i]
    print(ans)
    return _sum


def part2(data):
    return 2


def test():
    data = load_data("test_input.txt")
    assert part1(data) == 71
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
