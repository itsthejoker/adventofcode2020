from data import load_data

data = load_data()

x_pos, y_pos, trees = 0, 0, 0

def move(x, y):
    x += 3
    y += 1
    return x, y

for line in range(len(data)):
    x_pos, y_pos = move(x_pos, y_pos)
    try:
        treeline = data[y_pos]
    except:
        continue
    while len(treeline) < x_pos + 1:
        treeline += treeline
    if treeline[x_pos] == "#":
        trees += 1

print(trees)
