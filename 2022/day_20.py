from copy import copy

from functions.generic import *
from functions.load_data import load_data, load_data_int_array
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test
from time import sleep

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')
N = 0


class Node:
    def __init__(self, value=None, _next=None, previous=None):
        self.value = value
        self.next = _next
        self.previous = previous

    def get_new_nb(self, value, l):
        current = self
        # if not value % l:
        #     l -= 1
        if value < 0:
            for _ in range(-value % l):
                current = current.previous
            return current.previous, current
        else:
            for _ in range(value % l):
                current = current.next
            return current, current.next

    def get_result(self):
        current = self
        result = []
        for i in range(1, 3001):
            current = current.next
            if not i % 1000:
                result.append(current.value)
        return result

    def __str__(self):
        return f"{self.previous.value} <-> {self.value} <-> {self.next.value}"


def create_linked_list(data, multiplier):
    nodes = [Node(value=n * multiplier) for n in data]
    for previous, current, _next in zip([nodes[-1]] + nodes[:-1], nodes, nodes[1:] + [nodes[0]]):
        current.next = _next
        current.previous = previous
    return nodes


def mix(_data, multiplier=1, rounds=1):
    l = len(_data) - 1
    # print(_data)
    nodes = create_linked_list(_data, multiplier)

    for _ in range(rounds):
        for node in nodes:
            if not node.value:
                continue
            node.previous.next = node.next
            node.next.previous = node.previous
            _prev, _next = node.get_new_nb(node.value, l)
            if _prev == node:
                _prev = node.previous
            if _next == node:
                _next = node.next
            node.next = _next
            node.previous = _prev
            node.next.previous = node
            node.previous.next = node
    zero_node = [node for node in nodes if node.value == 0][0]
    return sum(zero_node.get_result())


def part1(data):
    return mix(data, multiplier=1, rounds=1)


def part2(data):
    return mix(data, multiplier=811589153, rounds=10)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=3, a2=1623178306, _load_data=load_data_int_array)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data_int_array(file_path)

    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
