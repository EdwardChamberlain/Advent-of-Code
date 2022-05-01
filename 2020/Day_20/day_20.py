import itertools
import jigsaw
import math

with open("Day_20/input_20.txt", 'r') as f:
    data = [i.split('\n') for i in f.read().split('\n\n')]

parsed_data = {}
for i in data:
    frame_id = i[0].split()[1][:-1]
    frame_data = [[p == '#' for p in n] for n in i[1:]]
    parsed_data[int(frame_id)] = frame_data

borders = {k:jigsaw.get_borders(v) for k, v in parsed_data.items()}
all_borders = []
for i in borders.values():
    all_borders.extend(i)
all_borders = [i for i in all_borders]

result = {}
for k, v in borders.items():
    result[k] = sum([jigsaw.number_of_matches(i, all_borders) for i in v])

corner_ids = [k for k, v in sorted(result.items(), key=lambda u: u[1]) if v == 2]
print(f"Pt1: {math.prod(corner_ids)}")