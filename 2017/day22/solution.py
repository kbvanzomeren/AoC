from copy import copy
from time import sleep


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    infected = {}
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == '#':
                infected[tuple([x, y])] = 3
    return len(data[0]) // 2, len(data) // 2, infected


class Virus:
    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected
        self.flagged = []
        self.weakened = []
        self.infected_count = 0
        self.d = 0

    def execute(self, bursts, evolved=False):
        for _ in range(bursts):
            if evolved:
                self.check_current_evolved()
            else:
                self.check_current()
            self.take_step()
        print(self.infected_count)

    def take_step(self):
        dx, dy = self.direction()
        self.x += dx
        self.y += dy

    def check_current(self):
        coord = tuple([self.x, self.y])
        if coord in self.infected and self.infected[coord] == 3:
            self.infected[coord] = 0
            self.right()
        else:
            self.infected[coord] = 3
            self.infected_count += 1
            self.left()

    def check_current_evolved(self):
        coord = tuple([self.x, self.y])
        if coord in self.infected:
            if self.infected[coord] == 3:
                self.infected[coord] = 2
                self.right()
            elif self.infected[coord] == 2:
                self.infected[coord] = 0
                self.back()
            elif self.infected[coord] == 1:
                self.infected[coord] = 3
                self.infected_count += 1
            elif self.infected[coord] == 0:
                self.infected[coord] = 1
                self.left()
        else:
            self.infected[coord] = 1
            self.left()

    def direction(self):
        return [[0, -1], [1, 0], [0, 1], [-1, 0]][self.d % 4]

    def left(self):
        self.d -= 1

    def right(self):
        self.d += 1

    def back(self):
        self.d += 2


def part1(data, bursts):
    virus = Virus(*data)
    virus.execute(bursts)
    return virus.infected_count


def part2(data, bursts):
    virus = Virus(*data)
    virus.execute(bursts)
    return virus.infected_count


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data, 10000) == 5587

    data = load_data("test_input.txt")
    assert part2(data, 100) == 26

    data = load_data("test_input.txt")
    assert part2(data, 10000000) == 2511944


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data, 10000)}")

    data = load_data("input.txt")
    print(f"Answer to part 2 is {part2(data, 10000000)}")
