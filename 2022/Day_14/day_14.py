import sys
import os
import numpy as np
import itertools
import operator
import cProfile


def vector_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def display_grid(grid):
    walls_locations = np.argwhere('#' == grid)

    start_col = min(walls_locations[:, 1]) - 3
    end_col = max(walls_locations[:, 1]) + 3

    start_row = 0
    end_row = max(walls_locations[:, 0]) + 3

    for i, d in enumerate(grid[start_row:end_row]):
        print(f"{i:>3}", ''.join(d[start_col:end_col]))


def condition_point(p):
    p = reversed(p)
    p = tuple(p)
    return p


def add_geometry(point_1, point_2, grid):
    y1, x1 = condition_point(point_1)
    y2, x2 = condition_point(point_2)

    x = sorted([x1, x2])
    y = sorted([y1, y2])

    grid[y[0]:y[1]+1, x[0]:x[1]+1] = '#'

    return grid


def simulate_sand(start, grid, max_depth) -> tuple[int]:
    current_location = start

    falling_vectors = [
        (1, 0),
        (1, -1),
        (1, 1),
    ]

    while True:
        if current_location[0] > max_depth:
            return None

        for v in falling_vectors:
            test_location = vector_add(current_location, v)

            if grid[test_location] == '.':
                current_location = test_location
                break

        else:
            break
    
    if current_location == start:
        return None

    return current_location


def pt_1(grid):
    max_depth = np.argwhere(grid == '#')[:, 0]
    max_depth = max(max_depth) + 3

    for i in itertools.count():
        
        result = simulate_sand(start_point, grid, max_depth)
        if result is None:
            break
        else:
            grid[result] = 'O'

    return i


def pt_2(grid):
    floor_height = max(np.argwhere(grid == '#')[:, 0]) + 2
    grid[floor_height, :] = '~'

    max_depth = np.argwhere(grid == '#')[:, 0]
    max_depth = max(max_depth) + 3

    for i in itertools.count():
        result = simulate_sand(start_point, grid, max_depth)
        if result is None:
            break
        else:
            grid[result] = 'O'

    return i+1

if __name__ == '__main__':
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = [d.split(' -> ') for d in data]
        data = [
            [list(map(int, p.split(','))) for p in d]
            for d in data
        ]

    grid = np.full((200, 1000), '.')

    start_point = (0, 500)
    grid[start_point] = '+'

    for lines in data:
        for line in itertools.pairwise(lines):
            grid = add_geometry(line[0], line[1], grid)

    # display_grid(grid)
    # print()

    print(pt_1(grid.copy()))
    print(pt_2(grid.copy()))
