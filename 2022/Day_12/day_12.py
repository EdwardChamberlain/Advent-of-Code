import sys
import os
import string
import numpy as np
import networkx as nx

def get_neighbours(row, col, grid) -> list[tuple[int]]:
    y, x = row, col
    neightbours = [
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1),
    ]
    for n in neightbours:
        if -1 in n:
            continue
        try:
            grid[n]
            yield n
        except IndexError:
            pass


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = [list(d) for d in data]

data = [
    [
        string.ascii_letters.index(r)
        for r in row
    ]
    for row in data
]

grid = np.array(data)

start = tuple(np.argwhere(grid == string.ascii_letters.index('S'))[0])
grid[start] = 0

end = tuple(np.argwhere(grid == string.ascii_letters.index('E'))[0])
grid[end] = string.ascii_letters.index('z')

G = nx.DiGraph()

x_len = grid.shape[0]
y_len = grid.shape[1]
for y, row in enumerate(grid):
    for x, g in enumerate(row):
        for neighbour in get_neighbours(y, x, grid):
            if grid[neighbour] <= g + 1:
                G.add_edge((y, x), neighbour)


# Pt 1
path = nx.astar_path(G, start, end)
print(len(path) - 1)


# Pt 2 
a_coords = np.argwhere(grid == string.ascii_letters.index('a'))
paths_from_as = []
for a in a_coords:
    start = tuple(a)
    try:
        x = nx.astar_path(G, start, end)
        paths_from_as.append(len(x) - 1)
    except:
        pass

print(min(paths_from_as))


exit()
output = []
for y, row in enumerate(data):
    output_row = []
    for x, col in enumerate(row):
        test = ()
        if (y, x) in path:
            output_row.append(1)
        else:
            output_row.append(0)
    output.append(output_row)

for o in output:
    for n in o:
        print(n, end=', ')
    print()
