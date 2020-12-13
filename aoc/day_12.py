from data import load_data

input = load_data()

input = [i for i in input.split('\n') if i != '']
CURRENT_DIRECTION = "E"
L_DIRECTIONS = ["E", "N", "W", "S"]
R_DIRECTIONS = ["E", "S", "W", "N"]

# [n/s, w/e]
CURRENT_LOCATION = [0, 0]
WAYPOINT_LOCATION = [1, 10]

def turn(current_dir: str, directive: str, amount: int) -> str:
    steps = int((amount / 90) % 4)
    if directive == "L":
        directions = L_DIRECTIONS
    elif directive == "R":
        directions = R_DIRECTIONS
    window_of_directions = (directions+directions)[
        directions.index(current_dir):directions.index(current_dir)+4
    ]
    return window_of_directions[steps]


def move(current_loc, directive, amount):
    if directive == "N":
        current_loc[0] += amount
    elif directive == "S":
        current_loc[0] -= amount
    elif directive == "E":
        current_loc[1] += amount
    elif directive == "W":
        current_loc[1] -= amount
    elif directive == "F":
        if CURRENT_DIRECTION == "N":
            current_loc[0] += amount
        elif CURRENT_DIRECTION == "S":
            current_loc[0] -= amount
        elif CURRENT_DIRECTION == "E":
            current_loc[1] += amount
        elif CURRENT_DIRECTION == "W":
            current_loc[1] -= amount
    return current_loc


for instruction in input:
    directive = instruction[:1].upper()
    amount = int(instruction[1:])
    if "L" in directive or "R" in directive:
        CURRENT_DIRECTION = turn(CURRENT_DIRECTION, directive, amount)
    else:
        CURRENT_LOCATION = move(CURRENT_LOCATION, directive, amount)

print(abs(CURRENT_LOCATION[0]), abs(CURRENT_LOCATION[1]))
print("--> ", abs(CURRENT_LOCATION[0]) + abs(CURRENT_LOCATION[1]))
