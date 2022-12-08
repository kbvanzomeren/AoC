# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def undo_rbl(password, ins, pl):
    for i in range(pl):
        attempt = password[i:] + password[:i]
        dx = attempt.find(ins[0]) + 1
        if dx >= 5:
            dx += 1
        dx %= pl
        attempt_scram = attempt[-dx:] + attempt[:-dx]
        if attempt_scram == password:
            return attempt

class Scrambler:
    def __init__(self, password, instructions, unscram):
        self.password = password
        self.instructions = instructions
        self.pl = len(password)
        self.unscram = unscram

    def run(self):
        if self.unscram:
            self.instructions.reverse()
        print(self.password)
        for (met, ins) in self.instructions:
            getattr(self, met)(ins)
            print(self.password)

    def sp(self, ins):
        x, y = ins
        a, b = self.password[x], self.password[y]
        _p = '|'
        self.password = self.password.replace(a, _p).replace(b, a).replace(_p, b)

    def sl(self, ins):
        a, b = ins
        _p = '|'
        self.password = self.password.replace(a, _p).replace(b, a).replace(_p, b)

    def rl(self, ins, run_rev=True):
        if self.unscram and run_rev:
            return self.rr(ins, run_rev=False)
        dx = ins[0]
        self.password = self.password[dx:] + self.password[:dx]

    def rr(self, ins, run_rev=True):
        if self.unscram and run_rev:
            return self.rl(ins, run_rev=False)
        dx = ins[0]
        self.password = self.password[-dx:] + self.password[:-dx]

    def rbl(self, ins):
        if self.unscram:
            self.password = undo_rbl(self.password, ins, self.pl)
            return
        dx = self.password.find(ins[0]) + 1
        if dx >= 5:
            dx += 1
        dx %= self.pl
        self.password = self.password[-dx:] + self.password[:-dx]

    def rp(self, ins):
        x, y = ins
        _pre = self.password[:x]
        _mid = self.password[x:y + 1][::-1]
        _suf = self.password[y + 1:]
        self.password = _pre + _mid + _suf

    def mp(self, ins):
        x, y = ins
        if self.unscram:
            y, x = ins
        a = self.password[x]
        if x < y:
            _pre = self.password[:y + 1].replace(a, '')
            _suf = self.password[y + 1:].replace(a, '')
        else:
            _pre = self.password[:y]
            _suf = self.password[y:].replace(a, '')
        # _mid = self.password[x:y + 1][::-1]
        self.password = _pre + a + _suf

def prep_data(data):
    instructions = []
    for line in data:
        line = line.replace('swap position', 'sp').replace(' with position', '')
        line = line.replace('swap letter', 'sl').replace(' with letter', '')
        line = line.replace('rotate left', 'rl').replace('rotate right', 'rr')
        line = line.replace('rotate based on position of letter', 'rbl').replace(' steps', '').replace(' step', '')
        line = line.replace('reverse positions', 'rp').replace(' through', '')
        line = line.replace('move position', 'mp').replace(' to position', '')
        splity = line.split(' ')
        instructions.append([splity[0], splity[1:]])


    for (ins, items) in instructions:
        if ins in ["sp", "rp", "rl", "rr", "mp"]:
            for i, item in enumerate(items):
                items[i] = int(item)
    return instructions


def part1(data):
    instructions = prep_data(data)
    # scarm = Scrambler('abcdefgh', instructions=instructions)
    scarm = Scrambler('abcde', instructions=instructions, unscram=False)
    scarm.run()

    return scarm.password


def part2(data):
    print()
    print()
    instructions = prep_data(data)
    scarm = Scrambler('fbgdceah', instructions=instructions, unscram=True)
    scarm.run()
    # scarm2 = Scrambler('fcgbdaeh', instructions=instructions)
    # scarm2.run(unscram=True)
    # print(scarm2.password)
    return scarm.password


if __name__ == "__main__":
    # undo_rbl('decab', ['d'])
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1='decab', a2='abcde')
    #
    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    # print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")