import sys
import os

def convert_range_to_list(x: str) -> str:
    x = x.split('-')
    x = list(map(int, x))
    x = list(range(x[0], x[1]+1))
    y = lambda x: '.' + str(x) + '.'
    x = ','.join(map(y, x))
    return x

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 
    data = [d.split(',') for d in data]

counter = 0 
for n, d in enumerate(data): 
    elf1 = convert_range_to_list(d[0])
    elf2 = convert_range_to_list(d[1])

    print(elf1)
    print(elf2)

    if elf1 in elf2 or elf2 in elf1:
        counter += 1
        print(True)

print(counter)
