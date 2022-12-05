import sys
import os
import re

def move_crate(cols: list, from_location: int, to_location: int) -> list:
    cols[to_location-1].append(cols[from_location-1].pop())
    return cols

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    start_positions, moves = data.split('\n\n') 

start_positions = start_positions.split('\n')
start_positions.reverse()

# Pt 1
cols = []
for n in range(9):
    col = [sp[n*4 + 1] for sp in start_positions[1:] if sp[n*4 + 1] != ' ']
    cols.append(col)

pattern = re.compile('move (.*) from (.*) to (.*)')
moves = moves.split('\n')
moves = [pattern.match(m).groups() for m in moves]
moves = [list(map(int, m)) for m in moves]

for m in moves:
    for i in range(m[0]):
        cols = move_crate(cols, m[1], m[2])

print(
    ''.join([c[-1] for c in cols])
)
