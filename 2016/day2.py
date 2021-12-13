# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


class Code:
    def __init__(self, x, y, data, weird_keypad):
        self.x = x
        self.y = y
        self.weird_keypad = weird_keypad
        self.data = data

    def get_position(self, line):
        dx = line.count('U') - line.count('D')
        dy = line.count('R') - line.count('L')
        self.x += dx
        self.y += dy
        if 0 <= self.x < 4 and 0 <= self.y < 4:
            return self.keypad()[self.y][self.x]

    def get_code(self):
        code= ''
        for line in self.data:
            for _m in line:
                getattr(self, _m)()

            if self.weird_keypad:
                code += str(self.keypad2()[self.y][self.x])
            else:
                code += str(self.keypad()[self.y][self.x])
        return code

    @staticmethod
    def keypad():
        return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


    @staticmethod
    def keypad2():
        return [
            [0, 0, 1, 0, 0],
            [0, 2, 3, 4, 0],
            [5, 6, 7, 8, 9],
            [0, 'A', 'B', 'C', 0],
            [0, 0, 'D', 0, 0],
        ]

    def check_output(self, dy, dx):
        if self.weird_keypad:
            is_valid = 0 <= self.x + dx < 5 and 0 <= self.y + dy < 5 and self.keypad2()[self.y + dy][self.x + dx]
        else:
            is_valid = 0 <= self.x + dx < 3 and 0 <= self.y + dy < 3

        if is_valid:
            self.x += dx
            self.y += dy

    def U(self):
        self.check_output(-1, 0)

    def D(self):
        self.check_output(1, 0)

    def L(self):
        self.check_output(0, -1)

    def R(self):
        self.check_output(0, 1)


def part1(data):
    return Code(1, 1, data, False).get_code()


def part2(data):
    return Code(0, 2, data, True).get_code()


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1='1985', a2='5DB3')

    file_path = INPUT_DIR + "day2a.txt"
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")