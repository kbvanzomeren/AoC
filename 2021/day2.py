# from functions.load_data import load_data
from functions.load_data import load_data_split_cast_to_int as load_data
# from functions.load_data import load_data
INPUT_DIR = "./inputs/"
TEST_INPUT_DIR = "./inputs_test/"


class Submarine:
    def __init__(self, commands):
        self.x = 0
        self.y = 0
        self.y_aim = 0
        self.aim = 0
        self.commands = commands

    def run_commands(self):
        for (movement, value) in self.commands:
            getattr(self, movement)(value)

    def forward(self, value):
        self.x += value
        self.y_aim += value * self.aim

    def up(self, value):
        self.y += value
        self.aim += value

    def down(self, value):
        self.y -= value
        self.aim -= value

    def depth(self, value):
        self.y += value

    def result(self):
        return self.x * -1 * self.y, self.x * -1 * self.y_aim


def prep_data(file):
    data = load_data(file)
    return [[_l.split(' ')[0], int(_l.split(' ')[1])] for _l in data]


def part1b(data):
    submarine = Submarine(commands=data)
    submarine.run_commands()
    return submarine.result()


def part1(data):
    coords = {
        "forward": 0,
        "down": 0,
        "up": 0,
    }
    for (key, value) in data:
        coords[key] += value
    return coords["forward"] * (coords["down"] - coords["up"])


def part2(data):
    aim = 0
    coords = {
        "forward": 0,
        "depth": 0,
    }

    for (key, value) in data:
        if key == "forward":
            coords['forward'] += value
            coords['depth'] += aim * value
        elif key == "down":
            aim += value
        elif key == "up":
            aim -= value
    return coords["forward"] * coords["depth"]


def test() -> None:
    test_file_path = TEST_INPUT_DIR + "day2a.txt"
    data = load_data(test_file_path, ' ')
    result_day_1 = part1(data)
    result_day_1b = part1b(data)
    result_day_2 = part2(data)

    print(f"Answer to test part 1 is {result_day_1}")
    assert result_day_1 == 150

    print(f"Answer to test part 1b is {result_day_1b[0]}")
    assert result_day_1b[0] == 150

    print(f"Answer to test part 2 is {result_day_2}")
    assert result_day_2 == 900

    print(f"Answer to test part 2 is {result_day_1b[1]}")
    assert result_day_1b[1] == 900


if __name__ == "__main__":
    test()

    file_path = INPUT_DIR + "day2a.txt"
    data = load_data(file_path, ' ')
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")