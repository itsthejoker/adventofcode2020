from data import load_data
from utilities.grid import Grid

data = load_data()
g = Grid(data)

x_pos, y_pos, trees = 0, 0, 0

# def move(x, y):
#     x += 3
#     y += 1
#     return x, y

for l in range(11):
    print(g.slope(3, 1))

# for line in range(len(data)):
#     x_pos, y_pos = move(x_pos, y_pos)
#     try:
#         treeline = data[y_pos]
#     except:
#         continue
#     while len(treeline) < x_pos + 1:
#         treeline += treeline
#     if treeline[x_pos] == "#":
#         trees += 1

# print(trees)
