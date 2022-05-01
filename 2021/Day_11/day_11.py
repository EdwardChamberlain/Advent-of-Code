tmp = [
    list('5483143223'),
    list('2745854711'),
    list('5264556173'),
    list('6141336146'),
    list('6357385478'),
    list('4167524645'),
    list('2176841721'),
    list('6882881134'),
    list('4846848554'),
    list('5283751526'),
]

tmp = [
    list('4764745784'),
    list('4643457176'),
    list('8322628477'),
    list('7617152546'),
    list('6137518165'),
    list('1556723176'),
    list('2187861886'),
    list('2553422625'),
    list('4817584638'),
    list('3754285662'),
]

# tmp = [
#     list('11111'),
#     list('19991'),
#     list('19191'),
#     list('19991'),
#     list('11111'),
# ]

FLASHES = 0

import itertools
DIMENSIONS = 2
ADJACENT_VECTORS = list(itertools.product(range(-1, 2), repeat=DIMENSIONS))
ADJACENT_VECTORS.remove(tuple((0 for _ in range(DIMENSIONS))))


converted = [
    [
        int(i)
        for i in row
    ]
    for row in tmp
]


def increment_array(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1
    return grid

def find_10s(grid):
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            try:
                if grid[y][x] >= 10:
                    result.append((x, y))
            except:
                pass
    return result

def cascade_10s(grid, flashes):
    for x, y in flashes:
        grid[y][x] = None
        for x_i, y_i in ADJACENT_VECTORS:
            x2 = x + x_i
            y2 = y + y_i
            if x2 < 0 or y2 < 0:
                continue
            try:
                grid[y2][x2] += 1
            except:
                pass
    return grid

def zero_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]  == None:
                grid[y][x] = 0
    return grid

def render_grid(grid):
    for i in grid:
        print(i)



grid = converted
for i in range(100):
    print(i+1)

    grid = increment_array(grid)

    while True:
        flashes = find_10s(grid)
        if flashes == []:
            break
        
        FLASHES += len(flashes)

        grid = cascade_10s(grid, flashes)

    grid = zero_grid(grid)
    render_grid(grid)
    print()

print(FLASHES)


# ~~ PT 2 ~~
grid = converted
for i in range(9999):
    FLASHES = 0
    print(i+101)

    grid = increment_array(grid)

    while True:
        flashes = find_10s(grid)
        if flashes == []:
            break
        
        FLASHES += len(flashes)

        grid = cascade_10s(grid, flashes)

    grid = zero_grid(grid)
    render_grid(grid)
    print(FLASHES)
    print()
    if FLASHES == 100:
        break

print(FLASHES)