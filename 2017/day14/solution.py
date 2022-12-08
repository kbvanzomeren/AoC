def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def knot_hash(data, n=256):
    _data = []
    for _c in data:
        _data.append(ord(_c))
    data = _data + [17, 31, 73, 47, 23]

    _l = 2 * list(range(n))
    current_postion = 0
    skip_size = 0
    for i in range(64):
        for _len in data:

            cp = current_postion % n
            ep = cp + _len

            _l = _l[:cp] + _l[cp:ep:][::-1] + _l[ep:]

            if ep >= n:
                __l = list(_l[n:n+cp]) + list(_l[cp:n])
                _l = 2 * list(__l)
            else:
                _l = 2 * list(_l[:n])
            current_postion += _len + skip_size
            skip_size += 1

    _c = chunks(_l[:n], 16)
    _nl = []
    for _sc in _c:
        _nl.append(eval(" ^ ".join([str(x) for x in _sc])))

    _hex = []
    for i in _nl:
        val = hex(i)[2:]
        if len(val) == 1:
            val = '0' + val

        _hex.append(val)
    return ''.join(_hex)


def load_data(key):
    data = []
    for i in range(128):
        ans = knot_hash(f'{key}-{i}')
        ans = '{:0128b}'.format(int(ans, 16))
        data.append(([int(c) for c in ans]))
    return data


def part1(data):
    return sum(sum(k) for k in data)


def get_valid_neighbours(data, current, visited):
    i, j = current
    nbs = []
    if 0 <= i - 1:
        nbs.append([i - 1, j])
    if 128 > i + 1:
        nbs.append([i + 1, j])
    if 0 <= j - 1:
        nbs.append([i, j - 1])
    if 128 > j + 1:
        nbs.append([i, j + 1])

    to_visit = []
    for nb in nbs:
        if nb not in visited and data[nb[0]][nb[1]]:
            to_visit.append(nb)
    return to_visit


def part2(data):
    visited = []
    groups = 0
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if [i, j] not in visited and data[i][j]:
                visited.append([i, j])
                to_visit = get_valid_neighbours(data, [i, j], visited)
                while to_visit:
                    next_visit = []
                    for tv in to_visit:
                        if tv not in visited:
                            visited.append(tv)
                            next_visit += get_valid_neighbours(data, tv, visited)
                    to_visit = next_visit
                groups += 1
                print(groups)

    return 2


def test() -> None:
    data = load_data("flqrgnkx")
    # data = load_data("a0c2017")
    assert part1(data) == 8108
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("jxqlasbh")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
