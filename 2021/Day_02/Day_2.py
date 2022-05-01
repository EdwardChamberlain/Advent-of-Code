with open('inputs/day_2.txt') as f:
    data = f.readlines()
    data = [d.strip().split(' ') for d in data]
    data = [(d[0], int(d[1])) for d in data]

for d in data:
    print(d)

x = 0
y = 0

for d, m in data:
    if d == 'forward':
        x += m
    elif d == 'backward':
        x -= m
    elif d == 'up':
        y -= m
    elif d == 'down':
        y += m

print(x, y)
print(x * y)

x = 0
y = 0
pitch = 0

for d, m in data:
    if d == 'forward':
        x += m
        y += m * pitch
    elif d == 'up':
        pitch -= m
    elif d == 'down':
        pitch += m

print(x, y)
print(x * y)