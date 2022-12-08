from functools import reduce
from operator import xor


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def part1(data, n = 256):
    _l = 2 * range(n)
    current_postion = 0
    skip_size = 0
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
    return _l[0] * _l[1]


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part2(data, n=256):
    _data = []
    for _c in data:
        _data.append(ord(_c))
    data = _data + [17, 31, 73, 47, 23]

    _l = 2 * range(n)
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
    # print(''.join(hex(i) for i in _nl))
    # print(''.join(hex(i).replace('0x', '  ') for i in _nl))
    _hex = []
    for i in _nl:
        val = hex(i)[2:]
        if len(val) == 1:
            val = '0' + val

        _hex.append(val)
    return ''.join(_hex)


def test():
    data = [3, 4, 1, 5]
    assert part1(data, 5) == 12

    data = ''
    assert part2(data) == 'a2582a3a0e66e6e86e3812dcb672a272'

    data = 'AoC 2017'
    assert part2(data) == '33efeb34ea91902bb2f59c9920caa6cd'

    data = '1,2,3'
    assert part2(data) == '3efbe78a8d82f29979031a4aa0b16a9d'

    data = '1,2,4'
    assert part2(data) == '63960835bcdc130f0b66d7ff4f6a5a8e'


if __name__ == "__main__":
    test()

    data = '76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229'

    # print("Answer to part 1 is ", part1(data))
    print("Answer to part 2 is ", part2(data))
