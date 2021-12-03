def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def load_data_int_array(file):
    with open(file, "r") as fd:
        data = [int(_l) for _l in fd.read().splitlines()]
    return data


def load_data_split(file, separator):
    with open(file, "r") as fd:
        data = [_l.split(separator) for _l in fd.read().splitlines()]
    return data


def load_data_split_cast_to_int(file, separator):
    data = load_data(file)
    result = []
    for line in data:
        result_line = []
        for item in line.split(separator):
            try:
                value = int(item)
            except:
                value = item
            result_line.append(value)
        result.append(result_line)
    return result
