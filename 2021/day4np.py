# from functions.load_data import load_data
from functions.generic import *
from functions.load_data import load_data
from functions.test import test
import numpy as np

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('np.py', 'a.txt')


def prep_data(data):
    rounds = np.fromstring(data[0], dtype=int, sep=',')
    cards_data = [i for i in data[2:] if i]
    cards = []
    for i in range(0, int(len(cards_data)), 5):
        cards.append(np.matrix(';'.join(cards_data[i:i+5])))
    return rounds, cards


def game(data, first_win):
    rounds, cards = prep_data(data)
    won_cards_index = []
    for number in rounds:
        for i, card in enumerate(cards):
            if number in card and i not in won_cards_index:
                card[card == number] = 0
                row_wins = card.sum(axis=0)
                col_wins = card.sum(axis=1)
                if 0 in row_wins or 0 in col_wins:
                    if first_win:
                        return number * card.sum()
                    else:
                        won_cards_index.append(i)
                        if len(won_cards_index) == len(cards):
                            return card.sum() * number


def part1(data):
    return game(data, first_win=True)


def part2(data):
    return game(data, first_win=False)


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=4512, a2=1924)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
