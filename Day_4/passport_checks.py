import re


def check_req_fields(entry):
    required_keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    for k in required_keys:
        if k not in entry.keys():
            return False
    return True

def check_birth(birth_string):
    return 1920 <= int(birth_string) <= 2002

def check_issue(issue_string):
    return 2010 <= int(issue_string) <= 2020

def check_expiry(expiry_string):
    return 2020 <= int(expiry_string) <= 2030

def check_height(height_string):
    height = re.search('(\d+)(in|cm)', height_string)

    if height is None:
        return False

    if height[2] == 'in':
        return 59 <= int(height[1]) <= 76

    elif height[2] == 'cm':
        return 150 <= int(height[1]) <= 193

    else: 
        return False

def check_hair(hair_string):
    if re.search('#[0-9|a-f]{6}', hair_string):
        return True
    else:
        return False

def check_eye(eye_string):
    valid = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth',
    ]

    for i in valid:
        if i == eye_string:
            return True
    return False

def check_id(id_string):
    if len(id_string) != 9:
        return False

    if id_string.isnumeric():
        return True
    else:
        return False