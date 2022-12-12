import string

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


HEIGHTS = {c: i for i, c in enumerate(string.ascii_lowercase, start=1)}
HEIGHTS['S'] = 1
HEIGHTS['E'] = 26

class MazeSolver:
    def __init__(self, data, position=[0, 0], visited=[], steps=0, target='X', is_reverted=False):
        self.data = data
        self.maze = data
        self.position = position
        self.bounds = [len(data[0]) - 1, len(data) - 1]
        self.visited = visited
        self.steps = steps
        self.target = target
        self.found_target = False
        self.is_reverted = is_reverted

    def find_start(self, start_char='0'):
        for y, row in enumerate(self.maze):
            for x, val in enumerate(row):
                if val == start_char:
                    self.position = [x, y]
                    return [x, y]

    def solve(self, target=None):
        current_moves = [self.position]

        # while not self.found_target:
        while not self.found_target:
            new_moves = []
            for move in current_moves:
                self.visited.append(move)
                new_moves += self.get_next_moves(move)
            current_moves = new_moves
            self.steps += 1

            self.check_end(current_moves)
        return self.steps

    def get_all_moves(self, position):
        x, y = position
        moves = []
        if 0 < x:
            moves.append([x - 1, y])
        if x < self.bounds[0]:
            moves.append([x + 1, y])
        if 0 < y:
            moves.append([x, y - 1])
        if y < self.bounds[1]:
            moves.append([x, y + 1])
        return moves

    def get_next_moves(self, position):
        valid_moves = []
        for move in self.get_all_moves(position):
            if self.check_move(position, move):
                self.visited.append(move)
                valid_moves.append(move)
        return valid_moves

    def check_move(self, position, move):
        if move in self.visited:
            return False
        current_char = HEIGHTS[self.maze[position[1]][position[0]]]
        next_char = HEIGHTS[self.maze[move[1]][move[0]]]
        if self.is_reverted and next_char + 1 < current_char:
            return False
        elif not self.is_reverted and next_char > current_char + 1:
            return False
        return True

    def check_end(self, next_moves):
        for move in next_moves:
            if self.maze[move[1]][move[0]] == self.target:
                self.found_target = True


def part1(data):
    maze = MazeSolver(position=[0, 0], data=data, visited=[], target='E')
    maze.find_start('S')
    steps = maze.solve()
    return steps


def part2(data):
    maze = MazeSolver(position=[0, 0], data=data, visited=[], target='a', is_reverted=True)
    maze.find_start('E')
    steps = maze.solve()
    return steps


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=31, a2=29)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
