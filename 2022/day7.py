from functions.generic import *
from functions.load_data import load_data
from functions.test import test

INPUT_DIR = f"./inputs/"
FILE_NAME = os.path.basename(__file__).replace('.py', 'a.txt')


def get_paths(path, new=""):
    if new:
        return "/".join(path), "/".join(path + [new])
    return "/".join(path[:-1]), "/".join(path)


def get_dir_structure(data):
    path = ["root"]
    structure = {"root": {"dirs": list(), "files": dict()}}
    i = 1
    len_data = len(data)
    while i < len_data:
        line = data[i]
        if "$ cd .." in line:
            path.pop()
        elif "$ cd" in line:
            path.append(line.split(' ')[-1])
            _path, next_path = get_paths(path)
            if next_path not in structure[_path]["dirs"]:
                structure[_path]["dirs"].append(next_path)
                structure[next_path] = {"dirs": list(), "files": dict()}
        elif "$ ls" in line:
            while True and i < len_data - 1:
                i += 1
                line = data[i]
                if "$ cd" in line:
                    i -= 1
                    break
                if "dir" in line[:3]:
                    _type, val = line.split(' ')
                    _path, next_path = get_paths(path, val)
                    if next_path not in structure[_path]["dirs"]:
                        structure[_path]["dirs"].append(next_path)
                        structure[next_path] = {"dirs": list(), "files": dict()}
                else:
                    _type, val = line.split(' ')
                    _, _path = get_paths(path)
                    structure[_path]["files"][val] = _type
        i += 1
    return structure


def calc_dir_size(dir_structure, current_dir, dir_sizes):
    if current_dir in dir_sizes:
        return dir_sizes[current_dir]
    size = sum([calc_dir_size(dir_structure, sub_dir, dir_sizes) for sub_dir in dir_structure[current_dir]["dirs"]])
    size += sum([int(val) for _, val in dir_structure[current_dir]["files"].items()])
    dir_sizes[current_dir] = size
    return size


def part1(data):
    dirs = get_dir_structure(data)
    dirs_sizes = {}
    calc_dir_size(dirs, "root", dirs_sizes)
    _sum = 0
    for key, value in dirs_sizes.items():
        if value <= 100000:
            _sum += value
    return _sum


def part2(data):
    dirs = get_dir_structure(data)
    dirs_sizes = {}
    calc_dir_size(dirs, "root", dirs_sizes)
    _sum = 0
    _min = 10e12
    req = 30000000 - (70000000 - dirs_sizes['root'])
    for key, value in dirs_sizes.items():
        if value >= req and value < _min:
            _min = value
    return _min


if __name__ == "__main__":
    test(file_name=FILE_NAME, part1=part1, part2=part2, a1=95437, a2=24933642)

    file_path = INPUT_DIR + FILE_NAME
    data = load_data(file_path)
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
