import sys
import os
import string


def chunk_list(x: list, chunk_size: int) -> list:
    for i in range(0, len(x), chunk_size):
        yield x[i: i + chunk_size]


def get_priority(item: str) -> int:
    return string.ascii_letters.index(item) + 1


# Get Data
with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')

# Pt 1
priorities = []
for rucksack in data:
    splitpoint = int(len(rucksack) / 2)
    comp_1 = rucksack[:splitpoint]
    comp_2 = rucksack[splitpoint:]

    for item in comp_1:
        if item in comp_2:
            priorities.append(get_priority(item))
            break
print(sum(priorities))

# Pt 2
priorities = []
for group in chunk_list(data, chunk_size=3):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            priorities.append(get_priority(item))
            break
print(sum(priorities))
