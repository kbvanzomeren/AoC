def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()
    return data


def load_data_split_empty(file, split_lines=True):
    result = []
    with open(file, "r") as fd:
        if split_lines:
            result = [block.splitlines() for block in fd.read().split("\n\n")]
        else:
            result = fd.read().split("\n\n")
    return result


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
