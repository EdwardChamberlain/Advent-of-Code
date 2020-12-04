import re
import passport_checks


with open("Day_4/input_4.txt", 'r') as f:
    data = f.read().split('\n\n')

data = [i.replace('\n', ' ') for i in data]

count = 0
for i in data:
    parsed = i.split()
    parsed = {i.split(":")[0]:i.split(":")[1] for i in parsed}

    if not passport_checks.check_req_fields(parsed):
        print('req', parsed)
        continue
    
    if not passport_checks.check_birth(parsed['byr']):
        print('birth', parsed)
        continue

    if not passport_checks.check_issue(parsed['iyr']):
        print('issue', parsed)
        continue

    if not passport_checks.check_expiry(parsed['eyr']):
        print('exp', parsed)
        continue

    if not passport_checks.check_height(parsed['hgt']):
        print('height', parsed)
        continue

    if not passport_checks.check_hair(parsed['hcl']):
        print('hair', parsed)
        continue

    if not passport_checks.check_eye(parsed['ecl']):
        print('eye', parsed)
        continue

    if not passport_checks.check_id(parsed['pid']):
        print('id', parsed)
        continue

    count += 1

print(f"Number of valid passports: {count}")
