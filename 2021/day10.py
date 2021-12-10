from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


mapper = {'{': '}', '[': ']', '(': ')', '<': '>'}
scores = {'}': 1197, ']': 57, ')': 3, '>': 25137}
scores2 = {'}': 3, ']': 2, ')': 1, '>': 4}


def check_chunk(line, get_invalid_score=True):
    ends = []
    for c in line:
        if c in mapper:
            ends.append(mapper[c])
        elif c == ends[-1]:
            ends.pop(-1)
        elif get_invalid_score:
            return scores[c]
        else:
            return
    if get_invalid_score:
        return 0
    return ends


def part1(data):
    score = 0
    for line in data:
        score += check_chunk(line)

    return score


def part2(data):
    valid_lines = [check_chunk(line, False) for line in data]
    valid_lines = [_vl for _vl in valid_lines if _vl]
    scores_result = []
    for _line in valid_lines:
        line = _line[::-1]
        score = 0
        for c in line:
            score *= 5
            score += scores2[c]
        scores_result.append(score)
    return sorted(scores_result)[int((len(scores_result) - 1) / 2)]


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=26397, a2=288957)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
