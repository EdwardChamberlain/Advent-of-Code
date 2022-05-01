import collections


def get_components(a, b):
    if a[1] == b[1]:
        start = min(a[0], b[0])
        end = max(a[0], b[0])
        x = range(start, end+1)
        y = [a[1]] * len(x)
        return tuple(zip(x, y))
    elif a[0] == b[0]:
        start = min(a[1], b[1])
        end = max(a[1], b[1])
        y = range(start, end+1)
        x= [a[0]] * len(y)
        return tuple(zip(x, y))
    else:
        if a[0] < b[0]:
            x = range(a[0], b[0]+1)
        else:
            x = range(a[0], b[0]-1, -1)

        if a[1] < b[1]:
            y = range(a[1], b[1]+1)
        else:
            y = range(a[1], b[1]-1, -1)

        return tuple(zip(x, y))


with open('2021/Day_05/input.txt') as f:
    data = f.read()
    data = data.split('\n')

parsed_data = [
    [tuple(map(int, k.split(','))) for k in i.split(' -> ')]
    for i in data
]

# ~~~~~~~~ PT 1 ~~~~~~~~
horizontal_only = [
    i
    for i in parsed_data
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]
]

counter = collections.Counter()
for d in horizontal_only:
    for pos in get_components(d[0], d[1]):
        counter[pos] += 1

crossings = {
    k:v   
    for k, v in counter.items()
    if v > 1
}
print(f"Horizontal Lines Only: {len(crossings)}")


# ~~~~~~~~ PT 2 ~~~~~~~~
counter = collections.Counter()
for d in parsed_data:
    for pos in get_components(d[0], d[1]):
        counter[pos] += 1

crossings = {
    k:v   
    for k, v in counter.items()
    if v > 1
}
print(f"All Lines: {len(crossings)}")