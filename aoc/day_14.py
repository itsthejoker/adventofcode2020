from data import load_data
import re

input = load_data()

def to_binary(integer:int) -> str:
    return "{0:b}".format(integer).zfill(36)

def to_int(binary) -> int:
    return int(binary, 2)

def apply_mask(mask, binary):
    binary = [_ for _ in binary]
    for count, i in enumerate(mask):
        if i == 'X':
            continue
        elif i == '0' or i == '1':
            binary[count] = i
    return ''.join(binary)

memory = {}

input = [i for i in input.split('\n')]

group_header = False
temp = []
groups = []
for line in input:
    if line == '':
        continue
    if 'mask' in line:
        if len(temp) > 0:
            groups.append(temp)
        temp = []
        group_header = True
        temp.append(line)
    if group_header:
        group_header = False
    else:
        temp.append(line)
groups.append(temp)

for g in groups:
    mask = g[0][g[0].index('=')+2:]
    for line in range(1, len(g)):
        address = re.search(r"mem\[([0-9]+)\]", g[line]).groups()[0]
        value = to_binary(int(g[line][g[line].index('=')+2:]))
        value = apply_mask(mask, value)
        print(address, value)
        memory[address] = value

values = []
for key, value in memory.items():
    values.append(to_int(value))

print(sum(values))

