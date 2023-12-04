
# Not mine
# def AG():
#     x = 516
#     while True:
#         x *= 16807
#         x %= 2147483647
#         if x % 4 == 0:
#             yield x
#
# def BG():
#     x = 190
#     while True:
#         x *= 48271
#         x %= 2147483647
#         if x % 8 == 0:
#             yield x
import time


def duel(a, b, am, bm, rem):
    return (a * am) % rem, (b * bm) % rem


def s_duel(x, xm, rem, rem2):
    while ((x * xm) % rem) % rem2:
        x = ((x * xm) % rem)
    return (x * xm) % rem


def part1(data, rangy=5):
    a, b, am, bm, rem = data
    eq = 0
    for i in range(rangy):
        a, b = duel(a, b, am, bm, rem)
        ab = "{:016b}".format(a)
        bb = "{:016b}".format(b)
        if ab[-16:] == bb[-16:]:
            eq += 1
    return eq


def part2(data, rangy=5):
    a, b, am, bm, rem = data
    eq = 0

    now = time.time()
    for i in range(rangy):
        a = s_duel(a, am, rem, 4)
        b = s_duel(b, bm, rem, 8)
        # ab = "{:016b}".format(a)
        # bb = "{:016b}".format(b)
        # if ab[-16:] == bb[-16:]:
        #     eq += 1
        # 1 * 2 ** 16 == 65536
        if a % 65536 == b % 65536:
            eq += 1
        if not i % 500000:
            print(i)
            print(time.time() - now)
    return eq


def test() -> None:
    data = [65, 8921, 16807, 48271, 2147483647]
    assert part1(data) == 1
    # assert part1(data) == 588
    assert part2(data, 5000000) == 309


if __name__ == "__main__":
    test()

    # data = load_data("input.txt")
    data = [516, 190, 16807, 48271, 2147483647]
    # print(f"Answer to part 1 is {part1(data, 40000000)}")
    # print(f"Answer to part 2 is {part2(data, 40000000)}")
    print(f"Answer to part 2 is {part2(data, 5000000)}")
