from data import load_data

input = load_data()

input = [i for i in input.split('\n') if i != '']

to_change = []

FREE = [".", "L"]
SEATS = ["L", "#", None]
TAKEN = ["#"]

PART_ONE = False


def slope(start_x, start_y, x, y):
    while True:
        if start_x + x < 0 or start_y + y < 0:
            return None
        try:
            next_step = input[start_x+x][start_y+y]
        except IndexError:
            next_step = None
        if next_step in SEATS:
            # print(f"{start_x=} {start_y=} {x=} {y=}")
            return next_step
        start_x += x
        start_y += y


def toggle(val):
    return "#" if val == "L" else "L"


def get_cell_state(x, y):
    cell = input[x][y]
    neighbors = []
    if PART_ONE:
        # grab the nine cells centered on our target
        for r in range(-1, 2):
            for c in range(-1, 2):
                try:
                    if x+r < 0 or y+c < 0:
                        raise IndexError
                    neighbors.append(input[x+r][y+c])
                except IndexError:
                    neighbors.append(None)
        # nuke the center because that's the target
        del neighbors[int(len(neighbors)/2)]
    else:
        neighbors.append(slope(x, y, 1, -1))  # NW
        neighbors.append(slope(x, y, 1, 0))  # N
        neighbors.append(slope(x, y, 1, 1))  # NE
        neighbors.append(slope(x, y, 0, -1))  # W
        neighbors.append(slope(x, y, 0, 1))  # E
        neighbors.append(slope(x, y, -1, -1))  # SW
        neighbors.append(slope(x, y, -1, 0))  # S
        neighbors.append(slope(x, y, -1, 1))  # SE

    # print(neighbors)
    taken, empty = 0, 0
    for n in neighbors:
        if n in TAKEN:
            taken += 1
        if n in FREE:
            empty += 1
    # print(f"{taken=} {empty=}")

    # rule time!
    if cell in FREE:
        if taken == 0:
            cell = toggle(cell)
    elif cell in TAKEN:
        if PART_ONE:
            if taken >= 4:
                cell = toggle(cell)
        else:
            if taken >= 5:
                cell = toggle(cell)
    return cell


def apply_changes_to_board(changes, board):
    # expand the board
    b_o_a_r_d = [[_ for _ in i] for i in board]
    for element in changes:
        b_o_a_r_d[element[0]][element[1]] = element[2]
    # deflate it back into the format we need
    board = [''.join(i) for i in b_o_a_r_d]
    return board

iterations = 0
from pprint import pprint as pp
while True:
    iterations += 1
    print(iterations)
    changes = []
    for row_count, row in enumerate(input):
        for col_count, col in enumerate(row):
            current_cell = input[row_count][col_count]
            if current_cell == ".":
                continue
            elif current_cell in ["#", "L"]:
                new_state = get_cell_state(row_count, col_count)
                if new_state != current_cell:
                    changes.append([row_count, col_count, new_state])
    if len(changes) > 0:
        # print(f"{changes=}")
        input = apply_changes_to_board(changes, input)
    else:
        print("Reached the end!")
        print(len([True for r in input for c in r if c in TAKEN]))
        break


# get_cell_state(4, 3)
# get_cell_state(0, 0)

# for row, line in enumerate(input):
#  print(row, line)