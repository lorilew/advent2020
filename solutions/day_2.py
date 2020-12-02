import re


def is_valid_old_policy(lower, upper, letter, password):
    only_letter = [l for l in password if l == letter]
    if int(lower) <= len(only_letter) <= int(upper):
        return True
    return False


def is_valid_new_policy(index1, index2, req_letter, password):
    letter1 = password[int(index1) - 1]
    letter2 = password[int(index2) - 1]
    if letter1 == req_letter and letter2 == req_letter:
        return False
    elif letter1 == req_letter or letter2 == req_letter:
        return True
    return False


with open('../resources/day_2_input.txt') as f:
    lines = f.readlines();

# PART 1
valid_count = 0
# PART 2
valid_count_new = 0
for text in lines:
    m = re.search("([0-9]+)-([0-9]+)\s([a-zA-Z]+):\s([a-zA-Z]+)", text)
    if is_valid_old_policy(*m.groups()):
        valid_count += 1
    if is_valid_new_policy(*m.groups()):
        valid_count_new += 1

print(valid_count)
print(valid_count_new)
