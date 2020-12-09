from data import load_data

input = load_data()
input = input.split("\n")
input = [i for i in input if i != ""]


def get_seat_id(row, col):
    return row * 8 + col


def chop(half, row_or_col):
    if half == 'F' or half == "L":
        return row_or_col[:int((len(row_or_col) - 1) / 2 + 1)]
    if half == 'B' or half == "R":
        return row_or_col[int((len(row_or_col) - 1) / 2 + 1):]


all_seat_ids = set()

for seat in input:
    rows = [i for i in range(128)]
    cols = [i for i in range(8)]
    row = seat[:7]
    col = seat[7:]
    for directive in row:
        rows = chop(directive, rows)
    row = rows[0]
    for directive in col:
        cols = chop(directive, cols)
    col = cols[0]
    seat_id = get_seat_id(row, col)
    all_seat_ids.update({seat_id})

for seat in range(80, 919):
    if seat not in all_seat_ids:
        print(seat)
