import os

import numpy as np


def printmap(map, mapper={0: ' ', 1: '#'}):
    for line in map:
        print(''.join([mapper[v] for v in line]))


def np_map(data, mapper={'.': 0, '#': 1}):
    return np.array([[mapper[v] for v in line] for line in data])
