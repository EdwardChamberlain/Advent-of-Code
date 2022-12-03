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

DRAW = [
    ['A', 'X'],
    ['B', 'Y'],
    ['C', 'Z'],
]

WIN_LOOKIP = dict(WIN)
LOSS_LOOKUP = dict(LOSS)
DRAW_LOOKUP = dict(DRAW)

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


# Pt 2
scores = []
for d in data:
    score = 0

    if d[1] == 'Z':
        score += SHAPE_POINTS[WIN_LOOKIP[d[0]]]
        score += 6
    elif d[1] == 'Y':
        score += SHAPE_POINTS[DRAW_LOOKUP[d[0]]]
        score += 3
    else:
        score += SHAPE_POINTS[LOSS_LOOKUP[d[0]]]
        score += 0

    scores.append(score)

print(sum(scores))