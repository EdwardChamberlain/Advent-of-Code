from functools import reduce


with open("Day_3/input_3.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

coeficients = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

counts = []

for r, d in coeficients:
    count = 0
    x = 0
    y = 0
    while True:
        if data[x][y % len(data[x])] == '#':
            count += 1
        x += d
        y += r
        if x >= len(data):
            break
    counts.append(count)

product = reduce((lambda x, y: x * y), counts)
print(f"Product = {product}")
