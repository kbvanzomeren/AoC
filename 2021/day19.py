import re
from collections import defaultdict

from functions.generic import *
from functions.load_data import load_data
# from functions.load_data import load_data_split_cast_to_int as load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def prep_data(data):
    result = {}
    for i, line in enumerate(data):
        if '--- scanner' in line:
            scanner_map = {}
            current_id = re.findall(r'\d+', line)[0]
        elif line:
            coord = [int(x) for x in line.split(',')]
            scanner_map[i] = {
                "coord": coord,
            }
        if not line:
            result[current_id] = scanner_map
    result[current_id] = scanner_map
    return calc_delta(result)


def calc_delta(result):
    for scanner, _map in result.items():
        for bid, beacon in _map.items():
            x1 = beacon["coord"]
            delta = {}
            for bid2, x2 in _map.items():
                if bid != bid2:
                     delta[bid2] = {"dc": [x1[0] - x2["coord"][0], x1[1] - x2["coord"][1], x1[2] - x2["coord"][2]],
                                    "d": sum([abs(x1[0] - x2["coord"][0]), abs(x1[1] - x2["coord"][1]),
                                              abs(x1[2] - x2["coord"][2])])}
            beacon["delta"] = delta
            beacon["dd"] = [x["d"] for _, x in beacon["delta"].items()]
    return result


def transfer_coords(data, sub_coords):
    new_coords = {bid: x for bid, x in data['0'].items()}
    scans_to_remove = []
    for sid, options in sub_coords.items():
        if options['rs'] == '0' and sid in data:
            scans_to_remove.append(sid)
            rs_pos = options['coord']
            tran = options['trans']
            for bid2, coord in data[sid].items():
                coord = coord['coord']
                new_coord = [rs_pos[j] + tran['S'][j] * coord[tran['T'][j]] for j in range(3)]
                if new_coord not in [x['coord'] for _, x in new_coords.items()]:
                    new_coords[bid2] = {"coord": new_coord}
    for _i in scans_to_remove:
        data.pop(_i)
    data['0'] = new_coords
    calc_delta(data)
    return data


def part(data):
    data = prep_data(data)
    sub_coords = {}
    i = 0
    while len(data) > 1:
        sid = '0'
        for sid2, _map2 in data.items():
            possible_coords = []
            if sid2 != sid:
                for bid, bdata in data[sid].items():
                    for bid2, bdata2 in _map2.items():
                        if sum([x in bdata2['dd'] for x in bdata['dd']]) > 10:
                            matches = []
                            for _did, _d in bdata['delta'].items():
                                if _d['d'] in bdata2['dd']:
                                    matches.append([_d, [_dd for _, _dd in bdata2['delta'].items() if _dd['d'] == _d['d']][0]])

                            for c1, c2 in matches[:1]:
                                if len(set(c1['dc'])) == 3:
                                    try:
                                        c1a = [abs(_c) for _c in c1['dc']]
                                        c2a = [abs(_c) for _c in c2['dc']]
                                        d1, d2, d3 = c1['dc']
                                        # d1a, d2a, d3a = c1a
                                        t1, t2, t3 = [c2a.index(_c) for _c in c1a]

                                        if 0 in c2['dc']:
                                            s1 = 1 if not c2['dc'][t1] else d1/c2['dc'][t1]
                                            s2 = 1 if not c2['dc'][t2] else d2/c2['dc'][t2]
                                            s3 = 1 if not c2['dc'][t3] else d3/c2['dc'][t3]
                                        else:
                                            s1, s2, s3 = d1/c2['dc'][t1], d2/c2['dc'][t2], d3/c2['dc'][t3]

                                        final = {
                                            "T": [t1, t2, t3],
                                            "S": [s1, s2, s3]
                                        }
                                        bc1 = bdata["coord"]
                                        bc2 = bdata2["coord"]
                                        possible_coords.append(
                                            [bc1[0] - s1 * bc2[t1], bc1[1] - s2 * bc2[t2], bc1[2] - s3 * bc2[t3]])
                                    except ValueError:
                                        pass
            p_coord = [x for x in possible_coords if possible_coords.count(x) > 3]

            if p_coord:
                sub_coords[sid2] = {
                    'coord': p_coord[0],
                    'trans': final,
                    'rs': sid
                }
        i += 1
        data = transfer_coords(data, sub_coords)
        new_sum = len(data['0'])
        print(new_sum)

    all_distances = []
    for bid, options in sub_coords.items():
        for bid2, options2 in sub_coords.items():
            if bid != bid2:
                all_distances.append(sum(abs(options['coord'][i] - options2['coord'][i]) for i in range(3)))
    print("part1: ", new_sum)
    print("part2", max(all_distances))
    return 1


def part2(data):
    return 2


if __name__ == "__main__":
    # test(file_name=FILE_NAME, part1=part1, part2=part2, a1=1, a2=2)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part(data)}")
