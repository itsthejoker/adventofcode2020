from data import load_data

input = load_data()
input = [int(i) for i in input.split('\n') if i != '']

max_joltage = max(input) + 3

input.append(max_joltage)
input.sort()

ones = sum([1 for count, item in enumerate(input) if not count+1 >= len(input) if input[count + 1] - item == 1])
threes = sum([1 for count, item in enumerate(input) if not count+1 >= len(input) if input[count + 1] - item == 3])

print("Part 1: ", ones*threes)


# With heavy influence and help from jnesslr. Need to rewrite to a proper recursive function.
cache = {0: 1}

for item in input:
    total = 0
    for i in range(item-3, item):
        if i not in cache:
            continue

        total += cache[i]
    cache[item] = total
print("Part 2: ", cache[max_joltage-3])
