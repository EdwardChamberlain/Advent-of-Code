import re


def check_pass(password):
    password = re.search('(\d+)-(\d+) ([a-z]): (.*)', password)

    count = password[4].count(password[3])

    if int(password[1]) <= count <= int(password[2]):
        return True
    else:
        return False


# Open Data
with open("Day_2/input_2.txt", 'r') as f:
    data = f.readlines()

good_passwords = [i for i in data if check_pass(i)]

print(f"Number of good passwords: {len(good_passwords)}")
