from time import sleep

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    results = []
    for line in data:
        split_line = line.split(' ')
        results.append(split_line)
    return results


class Assembunny:
    def __init__(self, d):
        self.data = d
        self.results = {"a": 12, "b": 0, "c": 0, "d": 0}
        self.line = 0

    def run_code(self):

        while self.line < len(self.data):
            try:
                dx = self.eval_line(self.data[self.line])
            except:
                dx = 1
            self.line += dx

    def get_value(self, _val):
        try:
            val = int(_val)
        except ValueError:
            val = self.results[_val]
        return val

    def eval_line(self, line):
        # print(line[0], line[1:])
        return getattr(self, line[0])(line[1:])

    def cpy(self, _input):
        self.results[_input[1]] = self.get_value(_input[0])
        return 1

    def inc(self, _input):
        d = 1
        s = 1
        if _input[0] == 'a' and self.line == 5:
            d = self.results['b'] * self.results['d']
            self.results['c'] = 0
            self.results['d'] = 0
            s = 5
        self.results[_input[0]] += d
        return s

    def dec(self, _input):
        self.results[_input[0]] -= 1
        return 1

    def jnz(self, _input):
        if self.get_value(_input[0]):
            return self.get_value(_input[1])
        return 1

    def tgl(self, _input):
        replacer = {
            "inc": "dec",
            "dec": "inc",
            "cpy": "jnz",
            "jnz": "cpy",
            "tgl": "inc"
        }
        check_i = self.get_value(_input[0]) + self.line
        # if check_i == self.line:
        #     self.data[check_i][0] = "inc"
        if check_i < len(self.data):
            self.data[check_i][0] = replacer[self.data[check_i][0]]

        return 1


def part1(data):
    _data = prep_data(data)
    ab = Assembunny(d=_data)
    ab.run_code()
    return ab.results.get("a")


def part2(data):
    return 2


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    # print(f"Answer to part 2 is {part2(data)}")
