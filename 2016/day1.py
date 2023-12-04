# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


class Position:
    def __init__(self, data, check_visited=False):
        self.x = 0
        self.y = 0
        self.d = 0
        self.data = [[c[0], int(c[1:])] for c in data[0].split(', ')]
        self.check_visited = check_visited
        self.visited = []

    def check_distance(self):
        for (dir, len) in self.data:
            getattr(self, dir)()
            _dir = self.direction()
            for _ in range(len):
                self.x += _dir[1]
                self.y += _dir[0]
                if self.check_visited and [self.x, self.y] not in self.visited:
                    self.visited.append([self.x, self.y])
                elif self.check_visited:
                    return abs(self.x) + abs(self.y)
        return abs(self.x) + abs(self.y)

    def direction(self):
        return [[1, 0], [0, 1], [-1, 0], [0, -1]][self.d % 4]

    def L(self):
        self.d -= 1

    def R(self):
        self.d += 1


def part1(data):
    return Position(data).check_distance()


def part2(data):
    return Position(data, True).check_distance()


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=8, a2=4)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)

    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")