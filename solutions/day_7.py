import re
first_regex = r'(\S+\s\S+)\sbags\scontain\s(.+)\.'
second_regex = r'\s?([0-9])\s(\S+\s\S+)\sbags?'

with open('../resources/day_7_input.txt') as f:
    rules = [r.replace('\n', '') for r in f.readlines()]

rule_tree = {}
for rule in rules:

    match = re.match(first_regex, rule)
    head = match.groups()[0]
    tailGroups = [re.match(second_regex, item) for item in match.groups()[1].split(',')]
    tail = [item.groups() for item in tailGroups if item]
    rule_tree[head] = { t[1]: t[0] for t in tail }

lookup_holder = {}
for outer, inner in rule_tree.items():
    for bag in inner:
        if bag in lookup_holder:
            lookup_holder[bag] += [outer]
        else:
            lookup_holder[bag] = [outer]


def outer_bag_options(bag_color):
    if bag_color not in lookup_holder:
        return [bag_color]
    else:
        result = set(lookup_holder[bag_color])
        for color in lookup_holder[bag_color]:
            containers = outer_bag_options(color)
            for c in containers:
                result.add(c)
        return result


print(len(outer_bag_options('shiny gold')))

def inner_bags(color):
    innies = rule_tree[color]
    if len(innies) == 0:
        return 1
    else:
        return sum([int(q) * inner_bags(color) for color, q in innies.items()]) + 1

print(inner_bags('shiny gold') -1 )

