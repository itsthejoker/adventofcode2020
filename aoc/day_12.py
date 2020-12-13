from typing import List

from data import load_data

input = load_data()

input = [i for i in input.split('\n') if i != '']
# CURRENT_DIRECTION = "E"
# L_DIRECTIONS = ["E", "N", "W", "S"]
# R_DIRECTIONS = ["E", "S", "W", "N"]

# [n/s, w/e]
CURRENT_LOCATION = [0, 0]
WAYPOINT_LOCATION = [1, 10]


def turn(waypoint_loc: List, directive: str, amount: int) -> List:
    def toggle_abs(val):
        if val >= 0:
            return -abs(val)
        else:
            return abs(val)

    steps = int((amount / 90) % 4)

    if directive == "L":
        for _ in range(steps):
            waypoint_loc = [waypoint_loc[1], toggle_abs(waypoint_loc[0])]
    elif directive == "R":
        for _ in range(steps):
            waypoint_loc = [toggle_abs(waypoint_loc[1]), waypoint_loc[0]]

    return waypoint_loc


def move(waypoint_loc: List, current_loc: List, directive, amount) -> [List, List]:
    if directive == "N":
        waypoint_loc[0] += amount
    elif directive == "S":
        waypoint_loc[0] -= amount
    elif directive == "E":
        waypoint_loc[1] += amount
    elif directive == "W":
        waypoint_loc[1] -= amount
    elif directive == "F":
        for _ in range(amount):
            current_loc = [current_loc[0] + waypoint_loc[0], current_loc[1] + waypoint_loc[1]]
    return waypoint_loc, current_loc

for instruction in input:
    directive = instruction[:1].upper()
    amount = int(instruction[1:])
    if "L" in directive or "R" in directive:
        WAYPOINT_LOCATION = turn(WAYPOINT_LOCATION, directive, amount)
    else:
        WAYPOINT_LOCATION, CURRENT_LOCATION = move(WAYPOINT_LOCATION, CURRENT_LOCATION, directive, amount)

print(abs(CURRENT_LOCATION[0]), abs(CURRENT_LOCATION[1]))
print("--> ", abs(CURRENT_LOCATION[0]) + abs(CURRENT_LOCATION[1]))
