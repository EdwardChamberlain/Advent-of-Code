import sys
import os
import functools

def get_views(row: int, col: int, data):
    left  = list(reversed(data[row][:col]))
    right = data[row][col+1:]
    up    = list(reversed([d[col] for d in data[:row]]))
    down  = [d[col] for d in data[row+1:]]
    return left, right, up, down


def is_visible(tree_height: list, views: list) -> bool:
    visibility = [is_visible_line(tree_height, v) for v in views]
    return any(visibility)


def is_visible_line(tree_height: int, view: list) -> bool:
    return tree_height > nmax(view)


def nmax(x: list):
    try:
        return max(x)
    except ValueError:
        return -1

def get_tree_factor(tree_height: int, views: list[int]) -> int:
    trees = [trees_in_view(tree_height, v) for v in views]
    return functools.reduce(lambda x, y: x*y, trees)


def trees_in_view(tree_height: int, view: list[int]) -> int:
    for n, v in enumerate(view):
        if v >= tree_height:
            return n + 1
    try:
        return n + 1
    except UnboundLocalError:
        return 0


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = [list(d) for d in data]
    data = [list(map(int, d)) for d in data]

# Pt 1
counter = 0
scenic_factors = []
for row, y in enumerate(data):
    for col, x in enumerate(y):
        tree  = data[row][col]
        views = get_views(row, col, data)

        if is_visible(tree, views):
            counter += 1

        scenic_factors.append(
            get_tree_factor(tree, views)
        )

print(counter) # Pt 1
print(max(scenic_factors)) # Pt 2
