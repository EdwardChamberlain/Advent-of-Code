import sys
import os
import string

import collections

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

