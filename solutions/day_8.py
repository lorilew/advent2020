with open('../resources/day_8_input.txt') as f:
    lines = [l.strip('\n') for l in f.readlines()]

def run(lines):
    acc = 0
    checklist = [i for i in range(0, len(lines))]

    current_line = 0
    exit_code = 0
    while (True):
        if current_line == len(checklist):
            # fini
            break
        if current_line > len(checklist) - 1:
            exit_code = 1
            break;
        if checklist[current_line] == 'X':
            exit_code = 1
            break;

        checklist[current_line] = 'X'
        args = lines[current_line].split(' ')
        if args[0] == 'nop':
            current_line += 1
        elif args[0] == 'jmp':
            current_line += int(args[1])
        elif args[0] == 'acc':
            current_line += 1
            acc += int(args[1])
        else:
            raise Error('Unknown command')

    return (exit_code, acc)

for i,line in enumerate(lines):
    args = line.split(' ')
    if args[0] == 'nop':
        current_line = 'jmp ' + args[1]
        (exit_code, acc) = run(lines[:i] + [current_line] + lines[i+1:])
        if exit_code == 0:
            print(acc)
            break
    elif args[0] == 'jmp':
        current_line = 'nop ' + args[1]
        (exit_code, acc) = run(lines[:i] + [current_line] + lines[i+1:])
        if exit_code == 0:
            print(acc)
            break
