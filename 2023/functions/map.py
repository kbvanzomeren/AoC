
def add_boundary(_map, boundary='.'):
    new_map = [boundary * (len(_map[0])  + 2)]
    for row in _map:
        new_map.append(boundary + row + boundary)
    new_map.append(boundary * (len(_map[0]) + 2))
    return new_map


def find_start(data, start_char='S'):
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == start_char:
                return x, y
