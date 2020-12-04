with open("Day_4/input_4.txt", 'r') as f:
    data = f.read().split('\n\n')

data = [i.replace('\n', ' ') for i in data]

count = 0
for i in data:
    parsed = i.split()
    parsed = {i.split(":")[0]:i.split(":")[1] for i in parsed}

    required_keys = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    missing_key = False
    for k in required_keys:
        if k not in parsed.keys():
            missing_key = True

    if missing_key is False:
        count += 1

print(f"Number of valid passports: {count}")
