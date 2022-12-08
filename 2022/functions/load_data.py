def load_data(file):
    """ Loads a text file and returns a list of lines in the file

    # input/day1.txt;
    Elf 1 has 2 power
    Elf 3 has 8 power
    1,2,3

    load_data(input/day1.txt)
    =>
    ["Elf 1 has 2 power", "Elf 3 has 8 power", "1,2,3"]

    :param file:
    :return: List of strings
    """
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def load_data_int_array(file):
    with open(file, "r") as fd:
        data = [int(_l) for _l in fd.read().splitlines()]
    return data


def load_data_int_array_filter(file, _filter='', _replace=[]):
    with open(file, "r") as fd:
        if _replace:
            data = [int(_l) if _l != _replace[0] else _replace[1] for _l in fd.read().splitlines()]
        else:
            data = [int(_l) for _l in fd.read().splitlines() if _l != _filter]
    return data


def load_data_split(file, separator=' '):
    with open(file, "r") as fd:
        data = [_l.split(separator) for _l in fd.read().splitlines()]
    return data


def load_data_split_cast_to_int(file, separator=',', one_list=True):
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
    if one_list:
        return result[0]
    return result
