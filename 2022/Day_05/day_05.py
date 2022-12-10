import sys
import os
import re
import copy


def move_crate(cols: list, from_location: int, to_location: int) -> list:
    cols[to_location-1].append(cols[from_location-1].pop())
    return cols


def move_crate_9001(cols: list, move: list[int]) -> list:
    number_of_crates, from_location, to_location = move
    buffer = [cols[from_location-1].pop() for _ in range(number_of_crates)]
    buffer.reverse()
    cols[to_location-1] += buffer
    return cols


# Get Data
with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    start_positions, moves = data.split('\n\n')

# Convert Start Data
start_positions = start_positions.split('\n')
start_positions.reverse()

cols = []
for n in range(9):
    col = [sp[n*4 + 1] for sp in start_positions[1:] if sp[n*4 + 1] != ' ']
    cols.append(col)

# Convert Moves data
pattern = re.compile('move (.*) from (.*) to (.*)')
moves = moves.split('\n')
moves = [pattern.match(m).groups() for m in moves]
moves = [list(map(int, m)) for m in moves]


# Pt 1
pt_1_cols = copy.deepcopy(cols)
for m in moves:
    for i in range(m[0]):
        pt_1_cols = move_crate(pt_1_cols, m[1], m[2])

print(
    ''.join([c[-1] for c in pt_1_cols])
)


# Pt 2
pt_2_cols = copy.deepcopy(cols)
for m in moves:
    pt_2_cols = move_crate_9001(pt_2_cols, m)

print(
    ''.join([c[-1] for c in pt_2_cols])
)
