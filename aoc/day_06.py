from data import load_data

input = load_data()

input = input.split('\n\n')

occurrences = {}
total_count = 0

print(input)

for count, group in enumerate(input):
    group = [i for i in group.split('\n') if i != '']
    occurrences[count] = {}
    occurrences[count]['size'] = len(group)
    for each in group:
        if each == "":
            continue
        for el in each:
            if not occurrences[count].get(el):
                occurrences[count][el] = 1
            else:
                occurrences[count][el] += 1

print(occurrences)

for group in occurrences:
    print(occurrences[group])
    answers = {key: value for key, value in occurrences[group].items() if key != 'size'}
    for k, v in answers.items():
        if v == occurrences[group]['size']:
            total_count += 1
print(total_count)
