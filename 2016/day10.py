import re
from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


class Bot:
    def __init__(self, _id):
        self.id = _id
        self.inventory = []
        self.lower_id = ''
        self.lower = None
        self.higher_id = ''
        self.higher = None
        self.separates = []

    def add_inventory(self, value=None, check_length=True):
        if value:
            self.inventory.append(value)

        if "bot" in self.id and check_length and len(self.inventory) == 2:
            _min = min(self.inventory)
            _max = max(self.inventory)
            self.separates.append(_min)
            self.separates.append(_max)
            # print(f"{self.id} passes value {_min} to {self.lower.id}")
            # print(f"{self.id} passes value {_max} to {self.higher.id}")
            self.lower.add_inventory(_min)
            self.higher.add_inventory(_max)

            self.inventory = []
        if len(self.inventory) == 2:
            return True
        return False

    # def get_or_create_share_bots(self, bots):
    #     should_revisit = False
    #     created_new = False
    #     if self.lower_id in bots:
    #         self.lower = bots[self.lower_id]
    #     elif self.lower_id:
    #         created_new = True
    #         self.lower = Bot(_id=self.lower_id)
    #     else:
    #         should_revisit = True
    #
    #     if self.higher_id in bots:
    #         self.higher = bots[self.higher_id]
    #     elif self.higher_id:
    #         created_new = True
    #         self.higher = Bot(_id=self.higher_id)
    #     else:
    #         should_revisit = True
    #
    #     return created_new, should_revisit


def get_or_create_slot(slots_dict, slots_id):
    if slots_id not in slots_dict:
        slots_dict[slots_id] = Bot(_id=slots_id)
    return slots_dict[slots_id]


def prep_data(data):
    slots_dict = {}
    for line in data:
        low = high = value = None
        if 'value' in line:
            value, bot = re.findall(r'\d+', line)
            bot = "bot_" + bot
        else:
            bot, low, high = line.replace(' gives low to ', ',').replace(' and high to ', ',').replace(' ', '_').split(',')
        bot = get_or_create_slot(slots_dict, bot)
        if value:
            start = bot.add_inventory(int(value), check_length=False)
            if start:
                start_bot = bot
        else:
            low = get_or_create_slot(slots_dict, low)
            high = get_or_create_slot(slots_dict, high)
            bot.lower = low
            bot.higher = high
    return slots_dict, start_bot


def part1(data):
    look_for = [17, 61]
    slots, start_bot = prep_data(data)
    start_bot.add_inventory()
    for _, slot in slots.items():
        if sorted(slot.separates) == look_for:
            return slot.id.strip('bot_')
    return 1


def part2(data):
    slots, start_bot = prep_data(data)
    start_bot.add_inventory()

    val1 = slots['output_0'].inventory[0]
    val2 = slots['output_1'].inventory[0]
    val3 = slots['output_2'].inventory[0]
    return val1 * val2 * val3


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)
    #
    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
