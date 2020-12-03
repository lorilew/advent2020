import math
def load_map():
    with open('../resources/day_3_input.txt') as f:
        lines = [l.replace('\n', '') for l in f.readlines()]
    return lines

def count_trees_encounters(stepx, stepy):
    map = load_map()
    height = len(map)
    width = len(map[0])
    ys = [y for y in range(0, height, stepy)]
    xs = [x for x in range(0, height*stepx, stepx)]

    trees = [map[y][x%width] for x,y in zip(xs,ys)]

    return len([t for t in trees if t == '#'])

# PART 1
print(count_trees_encounters(3, 1))

# PART 2
slopes = [
 (1,1),
 (3,1),
 (5,1),
 (7,1),
 (1,2)
]
print(math.prod([count_trees_encounters(*s) for s in slopes]))
