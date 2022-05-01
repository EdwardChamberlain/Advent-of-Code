from calendar import c
import re
import passport_checks


with open("2020/Day_04/input_4.txt", 'r') as f:
    data = f.read().split('\n\n')

data = [i.replace('\n', ' ').split() for i in data]
data = [{n.split(":")[0]:n.split(":")[1] for n in i} for i in data]

count = 0
for i in data:
    if passport_checks.check_req_fields(i):
        count += 1

print(f"Valid Passports (required fields): {count}")

count = 0
for i in data:
    if not passport_checks.check_req_fields(i):
        continue
    
    if not passport_checks.check_birth(i['byr']):
        continue

    if not passport_checks.check_issue(i['iyr']):
        continue

    if not passport_checks.check_expiry(i['eyr']):
        continue

    if not passport_checks.check_height(i['hgt']):
        continue

    if not passport_checks.check_hair(i['hcl']):
        continue

    if not passport_checks.check_eye(i['ecl']):
        continue

    if not passport_checks.check_id(i['pid']):
        continue

    count += 1

print(f"Number of valid passports: {count}")
