

class LoadData:
    def __init__(self, file, method='generic', seperator=' ', split_lines=True, _filter='', _replace=[], data=[],
                 skip=False):
        self.file = file
        self.seperator = seperator
        self.split_lines = split_lines
        self._filter = _filter
        self._replace = _replace
        self.method = method
        self.data = data
        self.skip = skip

    def read(self):
        if self.skip:
            return self.data
        getattr(self, self.method)()
        return self.data

    def generic(self):
        with open(self.file, "r") as fd:
            self.data = fd.read().splitlines()

    def int_array(self):
        """ Return list of ints"""
        with open(self.file, "r") as fd:
            self.data = [int(_l) for _l in fd.read().splitlines()]

    def int_arrays(self):
        """ Returns a list of list of ints
        => [[1, 2, 3], [4, 5, 6]
        """
        with open(self.file, "r") as fd:
            self.data = [[int(n) for n in _l.split(self.seperator)] for _l in fd.read().splitlines()]

    def split_blocks(self):
        """ Should deal with input if it contains blocks
        Elf ID 1
        Card 1: Blue 4
        Card 2: Blue 5

        Elf ID: 2
        Card 1: Green 4
        Card 2: Blue 4
        """
        with open(self.file, "r") as fd:
            if self.split_lines:
                result = [block.splitlines() for block in fd.read().split("\n\n")]
            else:
                result = fd.read().split("\n\n")
        return result


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


def load_data_int_array(file, multiple=False, seperator=' '):
    with open(file, "r") as fd:
        if multiple:
            data = [int(n) for _l in fd.read().splitlines() for n in _l.split(seperator)]
        else:
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
