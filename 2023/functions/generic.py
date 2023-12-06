import os


import numpy as np


def printmap(map, mapper={0: ' ', 1: '#'}):
    for line in map:
        print(''.join([mapper[v] for v in line]))


def np_map(data, mapper={'.': 0, '#': 1}):
    return np.array([[mapper[v] for v in line] for line in data])


import re


def get_numbers(line, remove='', cast_to_int=True):
    """Function that returns all numbers in a string
        "hello 42 I'm a -32 string 30"
        :return: [' 42', '-32', '30']
    """
    _regex = r'[+-]?\b\d+\b'

    if cast_to_int:
        return [int(number) for number in re.findall(_regex, line) if number != remove]
    else:
        return [number for number in re.findall(_regex, line) if number != remove]


# get digits
def get_digits(line, remove='', check_sign=True):
    """Function that returns all digits in a string
        "hello 42 I'm a -32 string 30"
        :return: ['4', '2', '3', '2', '3', '0']
    """
    if check_sign:
        return [number for number in re.findall(r'[-+]?\d', line) if number != remove]
    return [number for number in re.findall(r'\d', line) if number != remove]


import string
prio = {ch: i + 1 for i, ch in enumerate(string.ascii_lowercase + string.ascii_uppercase)}