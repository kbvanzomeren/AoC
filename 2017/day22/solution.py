
def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    infected = []
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == '#':
                infected.append([x, y])
    return infected, len(data[0]) // 2, len(data) // 2


class Virus:
    def __init__(self, x, y ,infected):
        self.x = x
        self.y = y
        self.infected = infected
        self.infected_count = 0
        self.d = 0

    def execute(self, bursts):
        for _ in range(bursts):


    def direction(self):
        return [[1, 0], [0, 1], [-1, 0], [0, -1]][self.d % 4]

    def L(self):
        self.d -= 1

    def R(self):
        self.d += 1


def part1(data):
    infected, x, y = data
    return 1


def part2(data):
    return 2


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 1
    assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
