import math

def get_row(min, max, codes):
    if (len(codes) == 0):
        return min
    elif (codes[0] == 'F'):
        diff = math.ceil((max - min)/2)
        return get_row(min, max - diff, codes[1:])
    elif (codes[0] == 'B'):
        diff = math.ceil((max - min)/2)
        return get_row(min + diff, max, codes[1:])
    else:
        raise Exception('Bad Row')

def get_col(min, max, codes):
    if (len(codes) == 0):
        return min
    elif (codes[0] == 'L'):
        diff = math.ceil((max - min)/2)
        return get_col(min, max - diff, codes[1:])
    elif (codes[0] == 'R'):
        diff = math.ceil((max - min)/2)
        return get_col(min + diff, max, codes[1:])
    else:
        raise Exception('Bad Col')

def get_seat(code):
    row = get_row(0,127, code[0:7])
    col = get_col(0,7, code[-3:])
    id = row * 8 + col
    return (row, col, id)

def get_boarding_passes():
    with open('../resources/day_5_input.txt') as f:
        lines = f.readlines()
    return [l.replace('\n', '') for l in lines]

# PART 1
occupied_seats_ids = [get_seat(b)[2] for b in get_boarding_passes()]
print(max(occupied_seats_ids))

def get_seating_plan(occupied_seats):
    seats = [[f'{(s,r,s*8 + r)}' for r in range(0,8)] for s in range(0,128)]

    for r,c,id in occupied_seats:
        seats[r][c] = '.'
    return seats

# PART 2
occupied_seats = [get_seat(b) for b in get_boarding_passes()]
seats = get_seating_plan(occupied_seats)
for r in seats:
    print(r)
