import itertools

RESULT = 2020

# Open Data
with open("Day_01/input_1.txt", 'r') as f:
    data = f.readlines()

# Convert to int
data = [int(i.strip()) for i in data]

# Search for pairs summing RESULT
results = [(x, y) for x, y in itertools.combinations(data, 2) if x + y == RESULT]
for i in results:
    print(f" {i[0]} + {i[1]} = {RESULT}!\n{i[0]} x {i[1]} = {i[0] * i[1]}", end='\n\n')

# Search for tripple summing RESULT
results = [(x, y, z) for x, y, z in itertools.combinations(data, 3) if x + y + z == RESULT]
for i in results:
    print(f" {i[0]} + {i[1]} + {i[2]} = {RESULT}!\n{i[0]} x {i[1]} x {i[2]}= {i[0] * i[1] * i[2]}", end='\n\n')
