import numpy as np

with open('day_1_input.txt') as f:
    lines = f.readlines()

nums = [int(l.replace('\n','')) for l in lines]

# PART 1
def part_1(target):
    for (i,n) in enumerate(nums):
        other_half = target - n

        if other_half in nums[i+1:]:
            return n * other_half
    return 0

print(part_1(2020));

# PART 2
for (i,n) in enumerate(nums):
    other_thirds = 2020 - n
    other_thirds_product = part_1(other_thirds)
    if other_thirds_product > 0:
        print(n * other_thirds_product)
        break;
