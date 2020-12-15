import random
import re

from data import load_data

input = load_data()


class MemoryAddress:
    def __init__(self, key):
        self.key = key
        self.k_e_y = [_ for _ in key]

    def calculate_possibles(self):
        #    __            _                                   _
        #   / _|          | |                                 (_)
        #  | |_ _   _  ___| | __  _ __ ___  ___ _   _ _ __ ___ _  ___  _ __
        #  |  _| | | |/ __| |/ / | '__/ _ \/ __| | | | '__/ __| |/ _ \| '_ \
        #  | | | |_| | (__|   <  | | |  __/ (__| |_| | |  \__ \ | (_) | | | |
        #  |_|  \__,_|\___|_|\_\ |_|  \___|\___|\__,_|_|  |___/_|\___/|_| |_|
        #
        # all my homies use monkey sort
        #
        total_possibilities = 2 ** len([_ for _ in self.k_e_y if _ == "X"])
        positions = [c for c, i in enumerate(self.k_e_y) if i == "X"]
        print(f"{total_possibilities=}")
        while True:
            temp = []
            for _ in range(total_possibilities ** 2):
                for p in positions:
                    self.k_e_y[p] = random.choice(["0", "1"])
                    temp.append(''.join(self.k_e_y))
            temp = set(temp)
            if len(temp) == total_possibilities:
                return temp


def to_binary(integer: int) -> str:
    return "{0:b}".format(integer).zfill(36)


def to_int(binary) -> int:
    return int(binary, 2)


def apply_mask(mask, binary, location=False):
    binary = [_ for _ in binary]
    for count, i in enumerate(mask):
        if location:
            if i == '0':
                continue
            elif i == 'X' or i == '1':
                binary[count] = i
        else:
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
        address = to_binary(int(re.search(r"mem\[([0-9]+)\]", g[line]).groups()[0]))
        addr = MemoryAddress(apply_mask(mask, address, location=True))
        addresses = [to_int(a) for a in addr.calculate_possibles()]
        value = to_binary(int(g[line][g[line].index('=')+2:]))
        for a in addresses:
            memory[a] = value

values = []
for key, value in memory.items():
    values.append(to_int(value))

print(sum(values))
