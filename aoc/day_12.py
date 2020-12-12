from data import load_data

input = load_data()

input = [i for i in input if i != '']

CURRENT_DIRECTION = "E"
L_DIRECTIONS = ["E", "N", "W", "S"]
R_DIRECTIONS = ["E", "S", "W", "N"]

CURRENT_LOCATION = [0, 0]

def turn(directive, amount):
    steps = (amount / 90) % 4
    if directive == "L":
        directions = L_DIRECTIONS
    if directive == "R":
        directions = R_DIRECTIONS
    directions = (directions+directions)[
        directions.index(CURRENT_DIRECTION):directions.index(CURRENT_DIRECTION)+4
    ]
    CURRENT_DIRECTION = directions[steps]


def move(directive, amount):
    pass


for instruction in input:
    directive = instruction[:1].lower()
    amount = int(instruction[1:])
    if "l" in directive or "r" in directive:
        turn(directive, amount)
    else:
        move(directive, amount)
