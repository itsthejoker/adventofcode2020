from data import load_data
from copy import copy
import re

input = load_data()

fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

def validate(field):
    key, value = field.split(":")[0], field.split(":")[1]
    if key == 'byr':
        value = int(value)
        return 1920 <= value <= 2002
    if key == 'iyr':
        value = int(value)
        return 2010 <= value <= 2020
    if key == 'eyr':
        value = int(value)
        return 2020 <= value <= 2030
    if key == 'hgt':
        integer = int(value[:-2])
        inttype = value[-2:]
        if inttype not in ['cm', 'in']:
            return False
        if inttype == 'cm':
            return 150 <= integer <= 193
        else:
            return 59 <= integer <= 76
    if key == 'hcl':
        regex = r"[a-f 0-9]{6}"
        return all([value.startswith('#'), len(value) == 7, bool(re.search(regex, value))])
    if key == "ecl":
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if key == "pid":
        regex = r"[0-9]{9}"
        return all([len(value) == 9, bool(re.search(regex, value))])
    return False


valid = 0

for item in input:
    print(item)
    print("********")
    item = item.split()
    itemfields = copy(fields)
    # breakpoint()
    for field in item:
        if field.split(":")[0] in fields:
            try:
                print(field, validate(field))
                if validate(field):
                    del itemfields[itemfields.index(field.split(":")[0])]
            except:
                continue
    print(len(itemfields))
    if len(itemfields) == 0:
        valid += 1

print(valid)

