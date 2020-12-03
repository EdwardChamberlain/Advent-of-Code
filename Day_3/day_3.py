with open("Day_3/input_3.txt", 'r') as f:
    data = f.readlines()
data = [i.strip() for i in data]

count = 0

for i, d in enumerate(data):
    loc = d[i*3 % len(d)]

    if loc == '#':
        count += 1

print(f"Trees hit: {count}")