
def add_boundary(_map, boundary='.'):
    new_map = [boundary * (len(_map[0])  + 2)]
    for row in _map:
        new_map.append('.' + row + '.')
    new_map.append(boundary * (len(_map[0]) + 2))
    return new_map