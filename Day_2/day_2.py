import re


def check_pass(password):
    p = re.search('(\d+)-(\d+) ([a-z]): (.*)', password)

    count = p[4].count(p[3])

    if int(p[1]) <= count <= int(p[2]):
        return True
    else:
        return False


def check_pass_2(password):
    p = re.search('(\d+)-(\d+) ([a-z]): (.*)', password)

    pos1 = p[4][int(p[1])-1] == p[3]
    pos2 = p[4][int(p[2])-1] == p[3]

    if pos1 != pos2:
        return True
    else:
        return False


# Open Data
with open("Day_2/input_2.txt", 'r') as f:
    data = f.readlines()

good_passwords = [i for i in data if check_pass(i)]
print(f"Number of good passwords using requirements 1: {len(good_passwords)}")

good_passwords = [i for i in data if check_pass_2(i)]
print(f"Number of good passwords using requirements 2: {len(good_passwords)}")
