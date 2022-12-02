import sys
import os

SHAPE_POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

WIN = [
    ['C', 'X'],
    ['A', 'Y'],
    ['B', 'Z'],
]

LOSS = [
    ['B', 'X'],
    ['C', 'Y'],
    ['A', 'Z'],
]

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 
    data = [d.split(' ') for d in data]

# Pt 1
scores = []
for d in data:
    score = 0

    score += SHAPE_POINTS[d[1]]

    if d in WIN:
        score += 6
    elif d in LOSS:
        ...
    else:
        score += 3

    scores.append(score)

print(sum(scores))