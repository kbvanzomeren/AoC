from functions import *

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


next_item = {
    1: lambda x, y, mx, my: [y, (x + 1) % mx],
    2: lambda x, y, mx, my: [(y + 1) % my, x],
}


def move(_map, y, x, i, new_map, has_changed):
    my, mx = _map.shape
    ny, nx = next_item[i](x, y, mx, my)
    if _map[ny][nx] == 0:
        new_map[y][x] = 0
        new_map[ny][nx] = i
        return True
    return has_changed


def part1(data):
    _map = np_map(data, {'.': 0, '>': 1, 'v': 2})
    new_map = deepcopy(_map)
    has_changed = True
    step = 0
    while has_changed:
        has_changed = False
        for i in [1, 2]:
            coords = np.where(_map == i)
            for y, x in zip(coords[0], coords[1]):
                has_changed = move(_map, y, x, i, new_map, has_changed)
            _map = new_map
            new_map = deepcopy(_map)
        step += 1
    return step


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=None, a1=58, a2=None)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
