import math
import itertools
from data import load_data

data = load_data()
data = [int(i) for i in data]

print("\nPart 1\n")

for first in data:
    for second in data:
        if first + second == 2020:
            result = first * second
print("Easy way: ", result)

# credit to Matt Perry for the idea
print("Hard way: ", math.prod([i for i in data if 2020-i in data]))

print("\nPart 2\n")

for first in data:
    for second in data:
        for third in data:
            if first + second + third == 2020:
                result = first * second * third
print(f"Easy way: {result}")

print("Hard way: ", set([a*b*c for a in data for b in data for c in data if a+b+c == 2020]))

# credit: jnesslr
print([a*b*c for a, b, c in itertools.combinations(data, 3) if a+b+c == 2020])
