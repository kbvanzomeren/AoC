with open('./inputs_test/day1a.txt', "r") as fd:
    data = fd.read().splitlines()


calories = []
elf = 0
for line in data:
    if line != '':
        elf = elf + int(line)
    elif line == '':
        calories.append(elf)
        elf = 0

print(max(calories))
