with open('inputs/day_1.txt') as f:
    data = f.readlines()
    data = [int(d.strip()) for d in data]

data = [
    (data[i] + data[i+1] + data[i+2])
    for i in range(len(data) - 2)
]

count = [
    True
    for i, d in enumerate(data)
    if i != 0 and d > data[i-1]
]

print(len(count))
