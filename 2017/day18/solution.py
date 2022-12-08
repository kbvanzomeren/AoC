from collections import defaultdict
from time import sleep


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    _data = []
    for line in data:
        blocks = line.split(' ')
        _data.append([blocks[0], blocks[1:]])
    return _data


class Duet:
    def __init__(self, instructions=[]):
        self.instructions = instructions
        self.register = defaultdict(lambda:0)
        self.frequency = 0

    def dance(self):
        l = len(self.instructions)
        i = 0
        while i < l:
            instruction, values = self.instructions[i]
            try:
                i += getattr(self, instruction)(values, self.register)
            except TypeError:
                return self.frequency

    def get_value(self, value, register):
        try:
            return int(value)
        except ValueError:
            return register[value]

    def set(self, values, register):
        x, y = values
        register[x] = self.get_value(y, register)
        return 1

    def add(self, values, register):
        x, y = values
        register[x] += self.get_value(y, register)
        return 1

    def mul(self, values, register):
        x, y = values
        register[x] *= self.get_value(y, register)
        return 1

    def mod(self, values, register):
        x, y = values
        register[x] %= self.get_value(y, register)
        return 1

    def snd(self, values, register):
        self.frequency = self.get_value(values[0], register)
        return 1

    def rcv(self, values, register):
        x = values[0]
        if self.get_value(x, register):
            if self.frequency:
                print(self.frequency)
                return 'Value error ;)'
        return 1

    def jgz(self, values, register):
        x, y = values
        if self.get_value(x, register) > 0:
            return self.get_value(y, register)
        return 1


class DuetParallel(Duet):
    def __init__(self, instructions):
        super().__init__(instructions)
        self.q0 = []
        self.q1 = []
        self.register0 = defaultdict(lambda: 0)
        self.register1 = defaultdict(lambda: 0)
        self.register0['p'] = 0
        self.register1['p'] = 1
        self.send_count = 0
        self.p = 0

    def dance(self):
        ins = [0, 0]
        while True:
            i = ins[self.p]

            instruction, values = self.instructions[i]
            queue = self.q0 if not self.p else self.q1
            register = self.register0 if not self.p else self.register1

            if instruction == "rcv" and not queue:
                self.p += 1
                if self.p == 2:
                    return self.send_count
            else:
                ins[self.p] += getattr(self, instruction)(values, register)

            if instruction == "snd" and self.p:
                self.p -= 1

    def snd(self, values, register):
        if self.p:
            self.send_count += 1
        queue = self.q0 if self.p else self.q1
        queue.append(self.get_value(values[0], register))
        return 1

    def rcv(self, values, register):
        queue = self.q0 if not self.p else self.q1
        register[values[0]] = queue[0]
        del queue[0]
        return 1


def part1(data):
    duet = Duet(instructions=data)
    return duet.dance()


def part2(data):
    duet = DuetParallel(instructions=data)
    return duet.dance()


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 4

    data = load_data("test_input2.txt")
    assert part2(data) == 3


if __name__ == "__main__":
    test()

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
