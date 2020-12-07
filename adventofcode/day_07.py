from data import load_data
from copy import deepcopy

input = load_data()

input = [i for i in input.split('\n') if i != '']

my_bag = "shiny gold"

bag_list = []

class Bag:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")
        self.allowed_storage = kwargs.get("allowed_storage")
        self.child_count = 0

    name = ""
    allowed_storage = {}

    def __repr__(self):
        return f"{self.name} - {self.allowed_storage}"


def parse_single_bag(bag):
    cleaned_bag = bag[:bag.index(' bag')].split()
    count = cleaned_bag[0]
    b_type = " ".join(cleaned_bag[1:])
    return count, b_type


def parse_rule(rule):
    full_contents = {}
    bag_type, contents = rule.split(' bags contain ')
    if "no other bags" in contents:
        return Bag(name=bag_type)
    if ", " in contents:
        contents = contents.split(", ")
        for bag in contents:
            count, b_type = parse_single_bag(bag)
            full_contents[b_type] = count
    else:
        count, b_type = parse_single_bag(contents)
        full_contents[b_type] = count
    return Bag(name=bag_type, allowed_storage=full_contents)

for rule in input:
    bag_list.append(parse_rule(rule))

part_one_colors = list()

bag_list_two = deepcopy(bag_list)

# clean the bag list, but only for part one
bag_list = [b for b in bag_list if b.allowed_storage is not None]
bag_list = [b for b in bag_list if b.allowed_storage != {}]

for bag in bag_list:
    if bag.allowed_storage is None:
        continue
    if my_bag in bag.allowed_storage:
        part_one_colors.append(bag)

# who has time for recursion
# for x in range(5):
#     print(x)
#     for b in bag_list:
#         for c in part_one_colors:
#             if c.name in b.allowed_storage:
#                 part_one_colors.append(b)


colors = set(part_one_colors)
colors_two = set(bag_list_two)

# print(colors)
print("Part 1: ", len(colors))

my_bag = [i for i in colors_two if i.name == 'shiny gold'][0]
my_bag_kids = []
for item in my_bag.allowed_storage.items():
    my_bag_kids.append([i for i in list(colors_two) if i.name == item[0]][0])

class Tree:
    def __init__(self, bag):
        self.tree = {}
        self.start = bag
        self.count = 0

    # apparently I have time for recursion >_<
    def populate_tree(self, tree=None):
        if not tree:
            tree = self.start

        if not tree.allowed_storage:
            tree.child_count = 0
            self.tree.update({tree: None})
            return
        kids = [
            [
                i for i in list(colors_two) if i.name == item[0]
            ][0] for item in tree.allowed_storage.items()
        ]
        self.tree.update({tree: kids})
        for item in kids:

            self.populate_tree(item)

            for _ in tree.allowed_storage.items():
                if _[0] == item.name:
                    if item.child_count == 0:
                        tree.child_count += int(_[1])
                    else:
                        tree.child_count += int(_[1]) * item.child_count + int(_[1])

t = Tree(my_bag)
t.populate_tree()

for item in t.tree:
    if item == t.start:
        print(item, item.child_count)
