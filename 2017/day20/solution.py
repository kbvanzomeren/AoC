import re
from math import factorial


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    results = []
    for line in data:
        results.append([int(d) for d in re.findall(r'-?\d+', line)])
    return results


def next_state(p):
    x, y, z, vx, vy, vz, ax, ay, az = p
    nvx = vx + ax
    nvy = vy + ay
    nvz = vz + az
    nx = x + nvx
    ny = y + nvy
    nz = z + nvz
    return [nx, ny, nz, nvx, nvy, nvz, ax, ay, az]


# def next_state_in_time(p, t):
#     x, y, z, vx, vy, vz, ax, ay, az = p
#     nx = x + (vx + t) + ax * t
#     nvx = vx + ax * t
#     ny = y + (vy + t) + ay * t
#     nvy = vy + ay * t
#     nz = z + (vz + t) + az * t
#     nvz = vz + az * t
#     return nx, ny, nz, nvx, nvy, nvz, ax, ay, az


def part1(data):
    _min = 1e99
    _min_p = 'x'
    poi = []
    for i, p in enumerate(data):
        _sum = sum([abs(x) for x in p[-3:]])
        if _sum <= _min:
            _min = _sum
            poi.append(i)

    if len(poi) == 1:
        state = data[poi[0]]
        print(state)
        for t in range(10):
            state = next_state(state)
            print(state)
        return poi[0]

    _min = None
    _min_p = 'x'
    npoi = []
    for p in poi:
        _sum = sum([abs(x) for x in data[p][3:-3]])
        if _min is None or _sum <= _min:
            _min = _sum
            npoi.append(p)
    npoi = []
    for p in poi:
        _sum = sum([abs(x) for x in data[p][3:-3]])
        if _min is None or _sum <= _min:
            _min = _sum
            npoi.append(p)
    return poi[0]


def part2(data):
    part_list = data
    for _ in range(1000):
        new_part_list = []
        for _, p in enumerate(part_list):
            new_part_list.append(next_state(p))

        coord_list = []
        remove = []
        for i, p in enumerate(new_part_list):
            if p[:3] in coord_list:
                ci = coord_list.index(p[:3])
                remove.append(ci)
                remove.append(i)
            coord_list.append(p[:3])
        part_list = [x for i, x in enumerate(new_part_list) if i not in remove]
        print(len(part_list))
    return 2


def test() -> None:
    data = load_data("test_input.txt")
    # assert part1(data) == 0
    data = load_data("test_input2.txt")
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
