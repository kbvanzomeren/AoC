
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    weights = {}
    tree_proc = {}

    all_childs = []

    for line in data:
        sub = line.split(' ')
        name = sub[0]
        weight = int(sub[1][1:-1])

        weights[name] = weight

        if '->' in line:
            children = line.split('->')[-1].replace(' ', '').split(',')
            tree_proc[name] = children
            all_childs += list(children)

    for key, _ in tree_proc.items():
        if key not in all_childs:
            print(key)

    return weights, tree_proc, all_childs


def part1(data):

    return 5


def part2():
    weights, tree_proc, all_childs = load_data("input.txt")

    items = []

    for _c in all_childs:
        if _c not in tree_proc:
            items.append(_c)
            items2 = list(items)

    not_changed = True
    while not_changed:
        not_changed = False
        for par, chil in tree_proc.items():
            if all(_chil in items for _chil in chil) and par not in items:
                n_weights = int(weights[par] + sum([weights[_child] for _child in chil]))
                weights[par] = n_weights

                t_w = weights[chil[0]]
                items.append(par)
                not_changed = True

    for par, chil in tree_proc.items():
        c0 = chil[0]
        t_w = weights[c0]
        if not all(weights[_child] == t_w for _child in chil) and c0 not in items2:
            print(chil)
            print([weights[_child] for _child in chil])
    return 2


def test():
    _data = load_data("test_input.txt")
    data = list(_data)
    assert part1(data) == 5
    data = list(_data)
    assert part2(data) == 2


if __name__ == "__main__":
    # test()
    _data = load_data("input.txt")
    data = list(_data)
    print(f"Answer to part 1 is {part1(data)}")
    # data = list(_data)
    print(f"Answer to part 2 is {part2()}")
