
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return [[x[0], int(x[1:])] for x in data]


def part1(data):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    dirs_xy = 0
    dx, dy = dirs[dirs_xy]

    x = 0
    y = 0

    for action, value in data:
        if action == 'N':
            x -= value
        elif action == 'S':
            x += value
        elif action == 'E':
            y += value
        elif action == 'W':
            y -= value
        elif action == 'F':
            x += dx * value
            y += dy * value
        elif action == 'R':
            steps = int(value / 90)
            dirs_xy = (dirs_xy + steps) % 4
            dx, dy = dirs[dirs_xy]
        elif action == 'L':
            steps = int(value / 90)
            dirs_xy = (dirs_xy - steps) % 4
            dx, dy = dirs[dirs_xy]

    return abs(x) + abs(y)


def rotate(action, value, ship_x, ship_y, way_x, way_y):
    rotation = 1 if action == 'R' else -1
    steps = int(value / 90) % 4
    if steps == 0:
        pass
    elif steps == 1:
        old_way_x = way_x
        way_x = rotation * way_y
        way_y = rotation * -1 * old_way_x
    elif steps == 2:
        way_x *= -1
        way_y *= -1
    elif steps == 3:
        old_way_x = way_x
        way_x = rotation * -1 * way_y
        way_y = rotation * old_way_x
    return way_x, way_y


def part2(data):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    dirs_xy = 0
    dx, dy = dirs[dirs_xy]

    ship_x = 0
    ship_y = 0

    way_x = -1
    way_y = 10

    for action, value in data:
        if action == 'N':
            way_x -= value
        elif action == 'S':
            way_x += value
        elif action == 'E':
            way_y += value
        elif action == 'W':
            way_y -= value
        elif action == 'F':
            ship_x += value * way_x
            ship_y += value * way_y
        elif action in ['R', 'L']:
            way_x, way_y = rotate(action, value, ship_x, ship_y, way_x, way_y)

        print(ship_x, ship_y)
        print(way_x, way_y)

    return abs(ship_x) + abs(ship_y)


def test():
    data = load_data("test_input.txt")
    assert part1(data) == 25
    assert part2(data) == 286


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
