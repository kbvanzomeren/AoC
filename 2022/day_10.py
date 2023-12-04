from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')
CHECK_CYCLE = list(range(20, (40 * 10 + 21) // 1, 40))


class Device:
    def __init__(self):
        self.register = {'x': 1}
        self.cycle = 0
        self.data = []
        self.total_signal = 0
        self.display = ['', '', '', '', '', '']
        self.sprite = range(3)

    def prep_data(self, data):
        self.data = [l.split(' ') for l in data]

    def run(self):
        for line in self.data:
            self.cycle += 1
            self.crt()
            getattr(self, line[0])(line[-1])
        return self.total_signal

    def crt(self):
        if self.cycle in CHECK_CYCLE:
            self.total_signal += self.register['x'] * self.cycle
        row = (self.cycle - 1) // 40
        self.display[row] += '#' if (self.cycle - 1) % 40 in self.sprite else ' '

    def noop(self, line):
        pass

    def addx(self, val):
        self.cycle += 1
        self.crt()
        self.register['x'] += int(val)
        self.sprite = range(self.register['x'] - 1, self.register['x'] + 2)

    def show_display(self):
        for row in self.display:
            print(row)


def part1(data):
    device = Device()
    device.prep_data(data)
    return device.run()


def part2(data):
    device = Device()
    device.prep_data(data)
    device.run()
    device.show_display()
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=13140, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
