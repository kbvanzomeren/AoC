# Prepare input
with open("test_input.txt", "r") as fd:
# with open("input.txt", "r") as fd:
    lists = []
    _list = []
    for line in fd.read().splitlines():
        if line:
            _list.append(line)
        else:
            lists.append(_list)
            _list = []
    lists.append(_list)

rules = {}
rules_relations = {}
rules_solved = {}
for rule in lists[0]:
    ind = rule.split(':')[0]
    rules[ind] = rule.split(': ')[1]
    if rule.split(': ')[1] == '"a"':
        rules_solved[ind] = ["a"]
    elif rule.split(': ')[1] == '"b"':
        rules_solved[ind] = ["b"]
    else:
        rules_relations[ind] = [_r for _r in rule.split(': ')[1].replace(' |', '').split(' ')]

rules['8'] += ' | 1001 | 1002 | 1003'
# rules['8'] += ' | 1001'
# results = lists[1]


# Part 1
def can_be_solved(ind):
    return all(_r in rules_solved for _r in rules_relations[ind])


def is_solved(current_item):
    _current_item = set(current_item.replace(' ', '').replace('|', ''))
    return all(_c in ['a', 'b'] for _c in _current_item)


def calc_options(options, result):
    for option in options:
        # print('-- OPTION --')
        # print(option)
        _results = []
        new_options2 = []
        for ind in option.split(' '):
            # print('-- CHAR --')
            # print(ind)
            new_options = rules_solved[ind]
            # print('-- NEW OPTIONS --')
            # print(new_options)
            if not _results:
                _results = new_options
            else:
                new_options2 = []
                for item1 in _results:
                    for item2 in new_options:
                        # print(item1, item2)
                        new_options2.append(item1 + item2)

            if new_options2:
                _results = new_options2
                new_options2 = []
        result += _results
    return result


for _ in range(20):
    for i, rule in rules.items():
        if i not in rules_solved and can_be_solved(i):
            # print('-- NEXT RULE --', i)
            result = list()
            calc_options(rule.split(' | '), result)
            rules_solved[i] = result
    if len(rules_solved) == len(rules):
        break

valid = [x for x in rules_solved['0'] if x in lists[1]]
valid2 = []
valid_sum = len(valid)

invalids = [x for x in lists[1] if x not in valid]

x1 = rules_solved['8']
x2 = rules_solved['11']
y1 = rules_solved['42']
y2 = rules_solved['31']

# print(len(x1[0]))
# print(len(x2[0]))
print(y1)
# print(len(y2[0]))

not_done = True
i = 0
while not_done:
    not_done = False
    invalid_blocks = []
    for _invalid in invalids:
        for
        if _invalid
        # print(len(_invalid))
        # print([len(_iii) for _iii in [_invalid[i * 5: i * 5 + 5] for i in range(20) if i * 5 < len(_invalid)]])

        d = len(x1[0])
        invalid_blocks.append([_invalid[i * d: i * d + d] for i in range(int(90/d)) if i * d < len(_invalid)])
    for blocks in invalid_blocks:
        if all(x in y1 for x in blocks):
            valid_sum += 1
            valid.append(''.join(blocks))
            valid2.append(''.join(blocks))

# valid_sum = len(valid)
for i in valid:
    print(i)

# invalids = [x for x in lists[1] if x not in valid]

# while not_done:
#     not_done = False
#     invalid_blocks = []
#     d1 = len(y1[0])
#     d2 = len(x1[0])
#     d3 = len(y2[0])
#     for _invalid in invalids:
#         _rinvalid = _invalid[:-1]
#         if len(_invalid) in [i*d1 + d2 + i*d3 for i in range(10)]:
#             invalid_blocks.append([[_invalid[i * d1: i * d1 + d1] for i in range(int(90/d1)) if i * d1 < len(_invalid)],
#                               # [_invalid[i * d1: i * d1 + d1] for i in range(int(90/d)) if i * d < len(_invalid)],
#                               [_rinvalid[i * d3: i * d3] for i in range(int(90/d3)) if i * d3 < len(_invalid)],
#                                    _invalid
#                               ])
#
#     for block1, block3, invalid in invalid_blocks:
#         counter = int((len(invalid) - d2) / (d1 + d3))
#         if all(y in y1 for y in block1) and all(y in y2 for y in block3):
#             valid_sum += 1
#             # valid.append(''.join(blocks))


