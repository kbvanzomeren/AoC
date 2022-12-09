from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


import re
result = re.findall(r'[-+]?\d*(?:.\d+)?', "hello 42 I'm a -32 string 30")
print(result)


def prep_data(data):
    moves = []
    for line in data:
        m, d = line.split(' ')
        moves.append([m, int(d)])
    return moves


class Simulation:
    def __init__(self, moves):
        self.moves = moves
        self.head = [0, 0]
        self.tail = [0, 0]

    def run(self, visited):
        for move, distance in self.moves:
            print(f"== {move} {distance} ==")
            for i in range(distance):
                getattr(self, move)()
                if self.tail not in visited:
                    visited.append([self.tail[0], self.tail[1]])
        print(len(visited))

    def R(self):
        self.head[0] += 1
        if abs(self.head[0] - self.tail[0]) <= 1:
            pass
        elif abs(self.head[0] - self.tail[0]) > 1 and self.head[1] != self.tail[1]:
            self.tail[1] = self.head[1]
            self.tail[0] += 1
        else:
            self.tail[0] += 1

    def L(self):
        self.head[0] -= 1
        if abs(self.head[0] - self.tail[0]) <= 1:
            pass
        elif abs(self.head[0] - self.tail[0]) > 1 and self.head[1] != self.tail[1]:
            self.tail[1] = self.head[1]
            self.tail[0] -= 1
        else:
            self.tail[0] -= 1

    def U(self):
        self.head[1] += 1
        if abs(self.head[1] - self.tail[1]) <= 1:
            pass
        elif abs(self.head[1] - self.tail[1]) > 1 and self.head[0] != self.tail[0]:
            self.tail[1] += 1
            self.tail[0] = self.head[0]
        else:
            self.tail[1] += 1

    def D(self):
        self.head[1] -= 1
        if abs(self.head[1] - self.tail[1]) <= 1:
            pass
        elif abs(self.head[1] - self.tail[1]) > 1 and self.head[0] != self.tail[0]:
            self.tail[1] -= 1
            self.tail[0] = self.head[0]
        else:
            self.tail[1] -= 1

def part1(data):
    moves = prep_data(data)
    sim = Simulation(moves)
    sim.run([])
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
