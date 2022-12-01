import advent_tools

import sys
import os

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n\n') 
    data = [d.strip() for d in data]
    data = [d.split('\n') for d in data]
    data = [list(map(float, d)) for d in data]

total = [sum(d) for d in data]

# pt 1
print(max(total))

# pt 2
print(
    sum(sorted(total, reverse=True)[:3])
)