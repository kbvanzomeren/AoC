import string

def load_data(file):
    instructions = []
    with open(file, "r") as fd:
        for ins in fd.read().splitlines()[0].split(','):
            dance = ins[0]
            moves = ins[1:].split('/')
            instructions.append([dance, moves])
    return instructions

class Dance:
    def __init__(self, instructions, line):
        self.instructions = instructions
        self.line = line

    def execute(self):
        # print(self.line)
        for ins, moves in self.instructions:
            positions = self.get_value(moves)
            getattr(self, ins)(moves, positions)
            # print(self.line)

    def get_value(self, moves):
        new_moves = []
        for move in moves:
            try:
                new_moves.append(int(move))
            except ValueError:
                new_moves.append(self.line.find(move))
        return new_moves

    def s(self, moves, positions):
        self.line = self.line[-positions[0]:] + self.line[:-positions[0]]

    def x(self, moves, positions):
        a = self.line[positions[0]]
        b = self.line[positions[1]]
        self.line = self.line.replace(b, '|').replace(a, b).replace('|', a)

    def p(self, moves, positions):
        a = moves[0]
        b = moves[1]
        self.line = self.line.replace(b, '|').replace(a, b).replace('|', a)


def part1(data, line):
    dance = Dance(data, line)
    dance.execute()
    return dance.line


def part2(data, line):
    dance = Dance(data, line)
    lines = [dance.line]
    _map = {0: dance.line}
    for i in range(1, 1000000001):
        dance.execute()
        _map[i] = dance.line
        if dance.line in lines:
            break
        lines.append(dance.line)
    return _map[int(1e9 % max(_map))]


def test() -> None:
    data = load_data("test_input.txt")
    line = 'abcde'
    assert part1(data, line) == 'baedc'
    # assert part2(data) == 2


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    line = string.ascii_lowercase[:16]
    print(f"Answer to part 1 is {part1(data, line)}")
    print(f"Answer to part 2 is {part2(data, line)}")
