import sys
import os

def convert_range_to_list(x: str) -> str:
    x = x.split('-')
    x = list(map(int, x))
    x = list(range(x[0], x[1]+1))
    y = lambda x: '.' + str(x) + '.'
    x = ','.join(map(y, x))
    return x

def conv_int(x):
    x = x.split('-')
    x = list(map(int, x))
    return x

# Pt 1
with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 
    data = [d.split(',') for d in data]

counter = 0 
for n, d in enumerate(data): 
    elf1 = convert_range_to_list(d[0])
    elf2 = convert_range_to_list(d[1])

    if elf1 in elf2 or elf2 in elf1:
        counter += 1

print(counter)

# Pt 2
count = 0
for n, d in enumerate(data):
    a = conv_int(d[0])
    b = conv_int(d[1])
    if a[0] < b[0]:
        x = a
        y = b
    else:
        x = b
        y = a

    if x[1] >= y[0]:
        count += 1

print(count)