import itertools


DIMENSIONS = 3
ADJACENT_VECTORS = list(itertools.product(range(-1, 2), repeat=DIMENSIONS))
ADJACENT_VECTORS.remove(tuple((0 for _ in range(DIMENSIONS))))


def render_cube(cube):
    for z in cube:
        for y in z:
            for x in y:
                print(x, end='')
            print()
        print()

def expand_z(cube: list):
    x_len = len(cube[0][0])
    y_len = len(cube[0])

    null_plane = ['.'*x_len] * y_len
    cube.insert(0, null_plane)
    cube.append(null_plane)

    return cube

def expand_xy(cube):
    result = []
    for cube_slice in cube:
        slice_result = ['.' + r + '.' for r in cube_slice]
        x_len = len(slice_result[0])
        slice_result = ['.'*x_len] + slice_result + ['.'*x_len]
        result.append(slice_result)
    return result

def expand_cube(cube):
    cube = expand_xy(cube)
    cube = expand_z(cube)
    return cube

def cycle_cube(cube):
    x_len = len(cube[0][0])
    y_len = len(cube[0])
    z_len = len(cube)

    print(x_len, y_len, z_len)

    res = cube.copy()

    for z in range(1, z_len-1):
        for y in range(1, y_len-1):
            for x in range(1, x_len-1):
                i = cube[z][y][x]
                neighbours_coords = get_neighbours_coords(x, y, z)
                neighbours = [
                    cube[v][k][i]
                    for i, k, v in neighbours_coords
                ]
                line= list(res[z][y])
                line[x] = state_change(i, neighbours)
                res[z][y] = line
    return res

def get_neighbours_coords(x, y, z):
    return [
        (x+v_x, y+v_y, z+v_z)
        for v_x, v_y, v_z in ADJACENT_VECTORS
    ]

def state_change(i, neighbours):
    active_neighbours = neighbours.count('#')

    if i == '.':
        if active_neighbours == 3:
            return '#'
        else:
            return '.'

    elif i == '#':
        if active_neighbours == 2 or active_neighbours == 3:
            return '#'
        else:
            return '.'

    else:
        raise ValueError("Dunno, shouldnt be here!")

def sum_active_states(cube):
    count = 0
    for z in cube:
        for y in z:
            for x in y:
                if x =='#':
                    count += 1
    return count


print()