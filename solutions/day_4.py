import re

def check_height(v):
    if 'cm' in v:
        return int(v[0:-2]) >= 150 and int(v[0:-2]) <= 193
    elif 'in' in v:
        return int(v[0:-2]) >= 59 and int(v[0:-2]) <= 76
    return False

required_fields = {
    'byr': lambda v : len(v) == 4 and int(v) >= 1920 and int(v) <= 2002,
    'iyr': lambda v : len(v) == 4 and int(v) >= 2010 and int(v) <= 2020,
    'eyr': lambda v : len(v) == 4 and int(v) >= 2020 and int(v) <= 2030,
    'hgt': lambda v : check_height(v),
    'hcl': lambda v : re.match(r'^\#[0-9a-zA-Z]{6}$', v),
    'ecl': lambda v : re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', v),
    'pid': lambda v : re.match(r'^[0-9]{9}$', v),
    # 'cid'
}

def get_passports():
    with open('../resources/day_4_input.txt') as f:
        lines = f.readlines() + ['\n'];

    buffer = ''
    passports = []
    for l in lines:
        if (len(buffer) > 0 and l == '\n'):
            passports += [buffer]
            buffer = ''
        else:
            buffer += l.replace('\n', ';').replace(' ', ';')
    return passports

def read_passport(passport):
    return {i.split(':')[0]:i.split(':')[1] for i in passport.split(';') if ':' in i}

def is_valid_v1(passport):
    for r in required_fields:
        if r not in passport:
            return False
    return True

def is_valid_v2(passport):
    for r in required_fields:
        if r not in passport:
            return False
        elif not required_fields[r](passport[r]):
            print(f'passport failed validation on {r}: {passport[r]}')
            return False

    return True

# PART 1
valid_v1_passports = [p for p in get_passports() if is_valid_v1(read_passport(p))]
print(len(valid_v1_passports))

# PART 2
valid_v2_passports = [p for p in get_passports() if is_valid_v2(read_passport(p))]
print(len(valid_v2_passports))
