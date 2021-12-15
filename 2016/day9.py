from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def part1(data):
    _s = data[0]
    end = ''
    m_start = _s.find('(')
    m_end = _s.find(')')
    while m_start != -1:
        end += _s[:m_start]
        l, m = _s[m_start + 1:m_end ].split('x')
        end += _s[m_end + 1: m_end + 1 + int(l)] * int(m)
        _s = _s[m_end + 1 + int(l):]
        m_start = _s.find('(')
        m_end = _s.find(')')
    end += _s
    return len(end)


def part2(data):
    _s = data[0]
    end = ''
    m_start = _s.find('(')
    m_end = _s.find(')')
    while m_start != -1:
        end += _s[:m_start]
        l, m = _s[m_start + 1:m_end ].split('x')
        _s = _s[m_end + 1: m_end + 1 + int(l)] * int(m) + _s[m_end + 1 + int(l):]
        m_start = _s.find('(')
        m_end = _s.find(')')
    end += _s
    return len(end)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=238, a2=445)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 1 is {part2(data)}")
