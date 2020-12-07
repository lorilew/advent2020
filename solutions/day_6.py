#
# def parse_input():
#     with open('../resources/day_6_input.txt') as f:
#         lines = f.readlines()+ ['\n'];
#
#     buffer = ''
#     group_ans = []
#     for l in lines:
#         if (len(buffer) > 0 and l == '\n'):
#             group_ans += [buffer]
#             buffer = ''
#         else:
#             buffer += l.replace('\n', '').replace(' ', '')
#     return group_ans
#
# def get_count_from_group(g):
#     return len(set(g))
#
# groups = parse_input()
#
# print(sum([get_count_from_group(g) for g in groups]))


def parse_input():
    with open('../resources/day_6_input.txt') as f:
        lines = f.readlines()+ ['\n'];

    buffer = ''
    group_ans = []
    for l in lines:
        if (len(buffer) > 0 and l == '\n'):
            group_ans += [buffer]
            buffer = ''
        else:
            buffer += l.replace('\n', ';')
    return group_ans

def get_count_from_group(g):
    answers = [set(a) for a in g[:-1].split(';')]
    if len(answers) == 1:
        return len(answers[0])
    else:
        return len(answers[0].intersection(*answers[1:]))



groups = parse_input()

print(sum([get_count_from_group(g) for g in groups]))
