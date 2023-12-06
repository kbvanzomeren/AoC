from copy import copy

from functions.generic import *
from functions.load_data import load_data, load_data_split_empty
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    results = []
    for line in data[0]:
        results.append(line)
    instructions = []
    number = ''
    for i in data[1][0]:
        if i.isdigit():
            number += i
        else:
            if number:
                instructions.append(int(number))
            instructions.append(i)
            number = ''
    if number:
        instructions.append(int(number))
    for i, coord in enumerate(results[0]):
        if coord != ' ':
            break
    current = [i, 0]

    for y, line in enumerate(results):
        for i, coord in enumerate(results[0]):
            if coord != ' ':
                break
        _min = [i, y]
        _max = [i, y]
        _min = [i for i, coord in enumerate(results[0]) if coord != ' ']

    return results, instructions, current
#
sides = [
    [4, 1, 2, 3],
    [4, 5, 2, 6],
]

def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


def get_cube_sides(_map, chunk_size=4):
    all_sides = []
    for x in split(_map, chunk_size):
        block_sides = [[], [], [], []]
        for j, line in enumerate(x):
            for i, side_line in enumerate(split(line, chunk_size)):
                block_sides[i].append(side_line)
        all_sides.append(block_sides)
    print(all_sides)







class Walk:
    def __init__(self, board, instructions, current):
        self.instructions = instructions
        self.board = board
        self.direction = 2
        self.current = current

    def run(self):
        for i, instruction in enumerate(self.instructions):
            if instruction == "R":
                self.direction += 1
            elif instruction == "L":
                self.direction -= 1
            else:
                for _ in range(instruction):
                    _continue, self.current = self.get_next(self.current)
                    if not _continue:
                        break
            # print(instruction, self.current)
            # if i > 600:
            #     break
            _da = 900
            if _da <= i <= _da + 100:
                print(instruction)
                print(i, *self.current)
                print(self.get_direction())
        return 1000 * (self.current[1] + 1) + 4 * (self.current[0] + 1) + (self.direction - 2) % 4

    def get_direction(self):
        return [(-1, 0), (0, -1), (1, 0), (0, 1)][self.direction % 4]

    def get_next(self, current):
        _direction = self.get_direction()
        old_direction = self.direction
        _next = (current[0], current[1])
        # while True:
        if self.direction % 2:
            _next = (current[0], _next[1] + _direction[1])
        else:
            _next = (current[0] + _direction[0], current[1])
        if _next[0] < 0 or _next[1] < 0:
            _next = self.teleport(_next)
        try:
            self.board[_next[1]][_next[0]]
        except IndexError:
            _next = self.teleport(_next)

        if self.board[_next[1]][_next[0]] == '#':
            self.direction = old_direction
            return False, self.current
        elif self.board[_next[1]][_next[0]] == ' ':
            _next = self.teleport(_next)
            if self.board[_next[1]][_next[0]] == '#':
                self.direction = old_direction
                return False, self.current
            return True, _next
        else:
            return True, _next
        print("Nonce?")

    def teleport(self, c):
        # c = self.current
        # Side one
        if c[0] == 49 and 0 <= c[1] < 50:
            _next = (0, 149 - c[1])
            self.direction += 2
        elif 50 <= c[0] < 100 and c[1] < 0:
            _next = (0, 150 + (c[0] - 50))
            self.direction += 1
        # Side two
        elif 100 <= c[0] < 150 and c[1] < 0:
            _next = (c[0] - 100, 199)
        elif c[0] == 150 and 0 <= c[1] < 50:
            _next = (99, 149 - c[1])
            self.direction += 2
        elif 100 <= c[0] < 150 and c[1] == 50:
            _next = (99, 50 + c[0] - 100)
            self.direction += 1
        # Side 3
        elif c[0] == 49 and 50 <= c[1] < 100:
            _next = (c[1] - 50, 100)
            self.direction -= 1
        elif c[0] == 100 and 50 <= c[1] < 100:
            _next = (100 + c[1] - 50, 49)
            self.direction -= 1
        # side 4
        elif 0 <= c[0] < 50 and c[1] == 99:
            _next = (50, 50 + c[0])
            self.direction += 1
        elif c[0] < 0 and 100 <= c[1] < 150:
            _next = (50, 49 - (c[1] - 100))
            self.direction += 2

        # side 5
        elif 50 <= c[0] < 100 and c[1] == 150:
            _next = (49, 150 + (c[0] - 50))
            self.direction += 1
        elif c[0] == 100 and 100 <= c[1] < 150:
            _next = (149, 49 - (c[1] - 100))
            self.direction += 2

        # side 6
        elif c[0] == 50 and 150 <= c[1] < 199:
            _next = (50 + (c[1] - 150), 149)
            self.direction -= 1
            x = 6
        elif 0 <= c[0] < 50 and c[1] == 200:
            _next = (100 + c[0], 0)
            x = 6
        elif c[0] < 0 and 150 <= c[1] < 200:
            _next = (50 + (c[1] - 150), 0)
            self.direction -= 1
            x = 6
        else:
            print("Unkonw case", self.current, c)
            c[87]
        return _next






def part1(data):
    _map, instructions, current = prep_data(data)
    board = Walk(_map, instructions, current)
    return board.run()
    # return 6032


def part2(data):
    _map, instructions, current = prep_data(data)
    get_cube_sides(_map)
    # board = Walk(_map, instructions, current)
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=6032, a2=2, _load_data=load_data_split_empty)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_split_empty(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
