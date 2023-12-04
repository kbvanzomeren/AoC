from functions.generic import *

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def cal_traj(dx, dy, xmin, xmax, ymin, ymax):
    xpos = 0
    ypos = 0
    while True:
        xpos += dx
        ypos += dy
        dy -= 1
        dx = dx - 1 if dx > 1 else 0
        if xmin <= xpos <= xmax and ymin <= ypos <= ymax:
            return 1
        if ypos < ymin or xpos > xmax:
            return 0


def calc_x(dx, xmin, xmax):
    xpos, lxpos, drag = 0, 0, 1
    while xpos <= xmax and dx != 0:
        lxpos = xpos
        xpos += dx
        dx = dx - 1 if dx > 1 else 0
    return xmin <= lxpos <= xmax


def part1(ymin):
    return sum(range(abs(ymin)))


def part2(data):
    xmin, xmax, ymin, ymax = data
    return sum(cal_traj(x, y, *data)
               for x in [dx for dx in range(xmin) if calc_x(dx, xmin, xmax)]
               for y in range(ymin, abs(ymin))) + \
           (xmax + 1 - xmin) * (abs(ymin) + 1 - abs(ymax))


if __name__ == "__main__":
    data = [244, 303, -91, -54]
    # print(f"Answer to part 1 is {part1(abs(data[2]) - 1)}")
    print(f"Answer to part 1 is {part1(abs(-10))}")
    print(f"Answer to part 1 is {part1(abs(data[2]))}")
    print(f"Answer to part 2 is {part2(data)}")
