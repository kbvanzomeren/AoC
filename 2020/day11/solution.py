from time import sleep

import numpy as np


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def part1(data):
    n_rows = len(data[0]) + 2
    n_collumns = len(data) + 2

    _map = np.zeros([n_collumns, n_rows])

    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                _map[i + 1][j + 1] = 0
            else:
                _map[i + 1][j + 1] = 2

    has_changed = True
    counter = 0
    while has_changed:
        take_seat = []
        empty_seat = []

        for i, row in enumerate(data):
            for j, seat in enumerate(row):
                if _map[i + 1, j + 1] == 2:
                    pass
                elif _map[i + 1, j + 1] == 1:
                    area = _map[i: i + 3, j:j + 3]
                    seats_taken = np.count_nonzero(area == 1)
                    seats_taken -= _map[i + 1][j + 1]
                    if seats_taken >= 4:
                        empty_seat.append([i + 1, j + 1])
                else:
                    area = _map[i: i + 3, j:j + 3]
                    seats_taken = np.count_nonzero(area == 1)
                    seats_taken -= _map[i + 1][j + 1]
                    if seats_taken == 0:
                        take_seat.append([i + 1, j + 1])

        if not take_seat and not empty_seat:
            has_changed = False

        for x, y in take_seat:
            _map[x, y] = 1

        for x, y in empty_seat:
            _map[x, y] = 0

        _mapper = {
            0: 'L',
            1: '#',
            2: '.',
        }

        counter += 1
        print(chr(27) + "[2J")
        print('=== current:', counter)
        for row in _map[1:-1, 1:-1]:
            print(''.join([_mapper[int(i)] for i in row]))
        print('')
        sleep(0.1)

    print(np.count_nonzero(_map == 1))
    return 1


def vision(_i, _j, data, x=0, y=0):
    n_rows = len(data[0]) + 2
    n_collumns = len(data) + 2

    counter = 1

    ans = []
    while 0 < _i + x * counter < n_collumns - 2 and 0 < _j + y * counter < n_rows - 2:
        try:
            if data[_i + x * counter][_j + y * counter] == 0:
                ans = [_i + x * counter, _j + y * counter]
                return ans
            counter += 1
        except IndexError:
            pass
    return ans



def part2(data):
    n_rows = len(data[0]) + 2
    n_collumns = len(data) + 2

    _mapper = {
        0: 'L',
        1: '#',
        2: '.',
    }

    _map = np.zeros([n_collumns, n_rows])

    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                _map[i + 1][j + 1] = 0
            elif seat == '#':
                _map[i + 1][j + 1] = 1
            else:
                _map[i + 1][j + 1] = 2

    for i, row in enumerate(_map):
        for j, seat in enumerate(row):
            try:
                if i == 0 or i == n_collumns - 1:
                    _map[i, j] = 2
                elif j == 0 or j == n_rows - 1:
                    _map[i, j] = 2
            except:
                pass

    visible_seat_map = {}

    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if _map[i + 1, j + 1] == 2:
                pass
            else:
                key = f"{i + 1}-{j + 1}"
                visible_seat_map[key] = []

                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=0 , y=-1))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=0 , y=1))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=1 , y=0))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=-1, y=0))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=-1, y=-1))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=-1, y=1))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=1 , y=1))
                visible_seat_map[key].append(vision(i + 1, j + 1, _map, x=1 , y=-1))

                visible_seat_map[key] = [xx for xx in visible_seat_map[key] if xx]

    has_changed = True
    counter = 0

    print(visible_seat_map['1-1'])
    print('=== current:', counter)
    # for row in _map[1:-1, 1:-1]:
    for row in _map:
        print(''.join([_mapper[int(i)] for i in row]))
    print('')

    while has_changed:
        take_seat = []
        empty_seat = []

        for i, row in enumerate(data):
            for j, seat in enumerate(row):
                if _map[i + 1, j + 1] == 2:
                    pass
                elif _map[i + 1, j + 1] == 1:
                    seats_taken = sum(_map[s[0], s[1]] for s in visible_seat_map[f"{i+1}-{j+1}"])
                    if seats_taken >= 5:
                        empty_seat.append([i + 1, j + 1])
                else:
                    seats_taken = sum(_map[s[0], s[1]] for s in visible_seat_map[f"{i+1}-{j+1}"])
                    if seats_taken == 0:
                        take_seat.append([i + 1, j + 1])

        if not take_seat and not empty_seat:
            has_changed = False

        for x, y in take_seat:
            _map[x, y] = 1

        for x, y in empty_seat:
            _map[x, y] = 0


        counter += 1
        print(chr(27) + "[2J")
        print('=== current:', counter)
        for row in _map[1:-1, 1:-1]:
            print(''.join([_mapper[int(i)] for i in row]))
        print('')
        sleep(0.1)

    print(np.count_nonzero(_map == 1))
    return 2


def test():
    data = load_data("test_input.txt")
    # assert part1(data) == 1
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
