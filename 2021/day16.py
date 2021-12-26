from typing import NamedTuple, Protocol

from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def converter(data):
    return ''.join([f'{int(h, 16):04b}' for h in data[0]])

# class _Packet(Protocol):
#     @property
#     def version(self):
#         pass


class Packet(NamedTuple):
    version: int
    type: int
    n: int = -1
    packets: tuple = ()


def read(i, n, b, is_int=False):
    if is_int:
        return i + n, int(b[i: i + n], 2)
    return i + n, b[i: i + n]


def parse_packet(i, b):
    while True:
        i, version = read(i, 3, b, True)
        i, _type = read(i, 3, b, True)
        if _type == 4:
            i, group = read(i, 5, b)
            n = 5
            result = group[1:]
            while group[0] == '1':
                i, group = read(i, 5, b)
                result += group[1:]
                n += 5
            return i, Packet(version=version, type=_type, n=int(result, 2))
        else:
            i, mode = read(i, 1, b, True)
            packets = []
            if not mode:
                i, length_sub = read(i, 15, b, True)
                j = i
                i += length_sub
                while j < i:
                    j, packet = parse_packet(j, b)
                    packets.append(packet)
            else:
                i, n_sub = read(i, 11, b, True)
                for _ in range(n_sub):
                    i, packet = parse_packet(i, b)
                    packets.append(packet)
            return i, Packet(version=version, type=_type, packets=tuple(packets))


def part1(data):
    b = converter(data)
    _, packet = parse_packet(0, b)
    packets = [packet]
    total = 0
    while packets:
        packet = packets.pop(0)
        total += packet.version
        packets.extend(packet.packets)
    return total


def get_value(packet):
    if packet.type == 0:
        return sum([get_value(sub_packet) for sub_packet in packet.packets])
    if packet.type == 1:
        return np.prod([1] + [get_value(sub_packet) for sub_packet in packet.packets])
    if packet.type == 2:
        return min([get_value(sub_packet) for sub_packet in packet.packets])
    if packet.type == 3:
        return max([get_value(sub_packet) for sub_packet in packet.packets])
    if packet.type == 4:
        return packet.n
    if packet.type == 5:
        return get_value(packet.packets[0]) > get_value(packet.packets[1])
    if packet.type == 6:
        return get_value(packet.packets[0]) < get_value(packet.packets[1])
    if packet.type == 7:
        return get_value(packet.packets[0]) == get_value(packet.packets[1])
    return get_value(packet)


def part2(data):
    b = converter(data)
    _, packet = parse_packet(0, b)
    return get_value(packet)



if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=16, a2=15)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
