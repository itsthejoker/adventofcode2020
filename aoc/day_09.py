from data import load_data

input = load_data()

input = [int(i) for i in input.split('\n') if i != '']

preamble_length = 25

for count, num in enumerate(input):
    if count < preamble_length:
        continue
    result = any([a + b == num for a in input[count-preamble_length: count] for b in input[count-preamble_length: count]])
    if not result:
        print("Found the number that doesn't belong")
        print(f"{count=}, {num=}")
        for window in range(600):
            for c in range(len(input)):
                if sum(input[c:c+window]) == num:
                    print("Possible answer: ", min(input[c:c+window])+max(input[c:c+window]))
