import re


def load_data(file):
    with open(file, "r") as fd:
        data = fd.read().splitlines()

    a = ''
    _data = []
    for line in data:
        if line:
            a += line
            a += ' '
        else:
            _data.append(a)
            a = ''
    _data.append(a[:-1])
    return _data


def part1(data):
    items = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = 0
    for passport in data:
        if all(x in passport for x in items):
            valid += 1
    return valid


def part2(data):
    items = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    hair = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid = 0
    inv = []
    for i, passport in enumerate(data):
        if all(x in passport for x in items):
            details = passport.split(' ')
            byr = [d for d in details if 'byr' in d][0].split(':')[1]
            _byr = 1920 <= int(byr) <= 2002 and len(byr) == 4

            iyr = [d for d in details if 'iyr' in d][0].split(':')[1]
            _iyr = 2010 <= int(iyr) <= 2020 and len(iyr) == 4

            eyr = [d for d in details if 'eyr' in d][0].split(':')[1]
            _eyr = 2020 <= int(eyr) <= 2030 and len(eyr) == 4

            hgt = [d for d in details if 'hgt' in d][0].split(':')[1]

            if 'cm' in hgt:
                _hgt = 150 <= int(hgt.replace('cm', '')) <= 193
            elif 'in' in hgt:
                _hgt = 59 <= int(hgt.replace('in', '')) <= 76
            else:
                _hgt = False

            hcl = [d for d in details if 'hcl' in d][0].split(':')[1]

            if hcl[0] == '#' and len(hcl) == 7:
                pattern = "^[a-f0-9]*$"
                _hcl = bool(re.match(pattern, hcl[1:]))
            else:
                _hcl = False

            ecl = [d for d in details if 'ecl' in d][0].split(':')[1]
            _ecl = ecl in hair

            pid = [d for d in details if 'pid' in d][0].split(':')[1]
            _pid = pid.isdigit() and len(pid) == 9

            if _byr and _iyr and _eyr and _hgt and _hcl and _ecl and _pid:
                valid += 1
            else:
                inv.append(i)
        else:
            inv.append(i)

    print(inv)
    return valid


def test() -> None:
    data = load_data("test_input.txt")
    assert part1(data) == 2

    data = load_data("valid.txt")
    part2(data)
    assert part2(data) == 4

    data = load_data("invalid.txt")
    part2(data)
    assert part2(data) == 0


if __name__ == "__main__":
    test()

    data = load_data("input2.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")

    data = load_data("input.txt")
    print(f"Answer to part 1 is {part1(data)}")
    print(f"Answer to part 2 is {part2(data)}")
