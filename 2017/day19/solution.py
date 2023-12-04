from time import sleep
import string
UPPERCASE = [x for x in string.ascii_uppercase]


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().split("\n")
    max_width = max([len(x) for x in data]) + 1
    results = []
    for line in data:

        results.append(line + ''.join([' ' for _ in range(max_width - len(line))]))

    start = data[0].find('|')
    return data, [start, 1], [start, 0]


def print_map(route, current):
    for i, line in enumerate(route):
        _line = line
        if i == current[1]:
            _line = line[:current[0]] + '8' + line[current[0] + 1:]
        print(_line)


class Board:
    def __init__(self, x, y, current, last, route):
        self.x = x
        self.y = y
        self.direction = [0, 1]
        self.direction_sym = '|'
        self.current = current
        self.last = last
        self.route = route
        self.max_y = len(route) - 1
        self.max_x = len(route[0])
        self.letters = ''
        self.n_steps = 1

    def run(self):
        while True:
            sleep(0.5)
            self.get_next_switch()

    def get_next_switch(self):
        i = 1
        while True:
            new_x = self.x + self.direction[0] * i
            new_y = self.y + self.direction[1] * i
            self.n_steps += 1
            if self.route[new_y][new_x] in UPPERCASE:
                self.letters += self.route[new_y][new_x]
                print(self.letters)
                print(self.n_steps)
            if self.route[new_y][new_x] == '+':
                self.x = new_x
                self.y = new_y
                # print_map(self.route, [self.x, self.y])
                self.rotate()
                break
            i += 1

    def rotate(self):
        x, y = self.x, self.y
        _u = [0, 1]
        _d = [0, -1]
        _l = [-1, 0]
        _r = [1, 0]
        moves = [_u, _d, _l, _r]

        new_dir = None
        for (dx, dy) in moves:
            try:
                if 0 < y + dy < self.max_y and 0 < dx + x and self.route[y + dy][x + dx] not in [' ', self.direction_sym] and [dx * -1, dy * -1] != self.direction:
                    new_dir = [dx, dy]
                    break
            except IndexError:
                pass

        if new_dir:
            self.direction = new_dir
            self.switch_direction()
        else:
            print(self.letters)
            int('s')

    def switch_direction(self):
        if self.direction_sym == '|':
            self.direction_sym = '-'
        else:
            self.direction_sym = '|'



def part1(data):
    route, current, last = data
    board = Board(*current, current, last, route)
    try:
        board.run()
    except:
        print(board.letters)
        print(board.n_steps - 1)
    return 1


def part2(data):
    return 2


def test() -> None:
    data = load_data("test_input.txt")
    # assert part1(data) == 1
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
