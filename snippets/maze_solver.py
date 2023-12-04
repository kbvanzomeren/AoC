def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


class MazeSolver:
    def __init__(self, maze, position=[0, 0], visited=[], steps=0, walls=['#'], target='X'):
        self.maze = maze
        self.position = position
        self.bounds = [len(maze[0]) - 1, len(maze) - 1]
        self.visited = visited
        self.steps = steps
        self.walls = walls
        self.target = target
        self.found_target = False

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
            if not current_moves:
                print(self.visited)
                print("Didn't find new moves")
                break
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
            if self.check_move(move):
                self.visited.append(move)
                valid_moves.append(move)
        return valid_moves

    def check_move(self, move):
        if move in self.visited:
            return False
        coord_char = self.maze[move[1]][move[0]]
        if coord_char in self.walls:
            return False
        return True

    def check_end(self, next_moves):
        for move in next_moves:
            if self.maze[move[1]][move[0]] == self.target:
                self.found_target = True

if __name__ == "__main__":
    # file_path = "./input_test.txt"
    file_path = "./input.txt"
    data = load_data(file_path)
    maze_1 = MazeSolver(position=[1, 1], maze=data, visited=[], target='1')
    maze_2 = MazeSolver(position=[1, 1], maze=data, visited=[], target='2')
    maze_3 = MazeSolver(position=[1, 1], maze=data, visited=[], target='3')
    maze_4 = MazeSolver(position=[1, 1], maze=data, visited=[], target='4')
    maze_1.find_start('0')
    steps = maze_1.solve()
    print(steps)
    maze_2.find_start('0')
    steps = maze_2.solve()
    print(steps)
    maze_3.find_start('0')
    steps = maze_3.solve()
    print(steps)
    maze_4.find_start('0')
    steps = maze_4.solve()
    print(steps)
