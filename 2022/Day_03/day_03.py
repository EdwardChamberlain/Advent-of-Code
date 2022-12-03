import sys
import os
import string

# Get Data
with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 

# Pt 1
priorities = []
for d in data:
    splitpoint = int(len(d) / 2)
    a = d[:splitpoint]
    b = d[splitpoint:]

    for i in a:
        if i in b:
            priorities.append(string.ascii_letters.index(i) + 1)
            break

print(sum(priorities))

# Pt 2
def chunk_list(x: list, chunk_size: int) -> list: 
    for i in range(0, len(x), chunk_size):
        yield x[i: i + chunk_size]


priorities = []
for group in chunk_list(data, chunk_size=3):
    for i in group[0]:
        if i in group[1] and i in group[2]:
            priorities.append(string.ascii_letters.index(i) + 1)
            break

print(sum(priorities))
