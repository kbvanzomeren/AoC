import numpy as np

def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def get_coords(ticket):
    ticket = ticket.replace('F', '0')
    ticket = ticket.replace('B', '1')
    ticket = ticket.replace('L', '0')
    ticket = ticket.replace('R', '1')
    return int(ticket[:7], 2), int(ticket[7:], 2)


def get_ids(data):
    ids = []
    for ticket in data:
        row, column = get_coords(ticket)
        ids.append(row * 8 + column)
    return ids


def part1(data):
    return max(get_ids(data))


def part2(data):
    _map = np.zeros((128, 8))

    for ticket in data:

        row, column = get_coords(ticket)
        _map[row][column] = 1

    empty_seats = np.transpose(np.where(_map == 0))
    for x, y in empty_seats:
        if x > 0 and x < 127 and _map[x-1][y] == 1 and _map[x+1][y] == 1 and _map[x][y-1] == 1 and _map[x][y+1] == 1:
            ans = x * 8 + y

    return ans


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 820
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
