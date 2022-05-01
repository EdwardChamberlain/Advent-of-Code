from functools import reduce


with open("Day_03/input_3.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
)

results = []
for slope_x, slope_y in slopes:
    x, y = 0, 0
    count = 0
    while True:
        if data[y][x % len(data[y])] == '#':
            count += 1
        
        x += slope_x
        y += slope_y

        if y >= len(data):
            break

    results.append(count)
    print(f"Slope: ({slope_x}, {slope_y}) = {count}")

product = reduce((lambda x, y: x * y), results)
print(f"Product = {product}")
