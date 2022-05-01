## This whole script is a steaming pile of garbage and if you are reading this I emplore you to look elsewhere for any semblance of competence. 
##
## Oh and it takes ages to solve.

import itertools


DIMENSIONS = 4
ADJACENT_VECTORS = list(itertools.product(range(-1, 2), repeat=DIMENSIONS))
ADJACENT_VECTORS.remove(tuple((0 for _ in range(DIMENSIONS))))


def add_vect(coord, vector):
    return tuple((i[0] + i[1] for i in zip(coord, vector)))

def get_all_adjacent(coord):
    return [add_vect(coord, i) for i in ADJACENT_VECTORS]

def get_adjacent_values(coord, core_map):
    return [core_map[i] for i in get_all_adjacent(coord) if i in core_map]

def count_active_adjacents(coord, core_map):
    return len([i for i in get_adjacent_values(coord, core_map) if i ==True])

def update_state(coord, core_map):
    acitves = count_active_adjacents(coord, core_map)

    if core_map[coord] == True:
        return 2 <= acitves <= 3
    else:
        return acitves == 3

def import_input(problem_input, cycles):
    xy_dim = list(range(-(len(problem_input)+cycles), (len(problem_input)+cycles + 1)))
    n_dim  = list(range(-(cycles), +(cycles+1))) 
    n_dims = list(itertools.product(n_dim, repeat=DIMENSIONS-2))

    coords = []
    for n in n_dims:
        for x in xy_dim:
            for y in xy_dim:
                coords.append(build_flat_plane_coord(x, y, n))

    core_map = {}
    for i in coords:
        core_map[i] = False

    for i, row in enumerate(problem_input):
        for n, val in enumerate(row):
            core_map[build_flat_plane_coord(i-1, n-1)] = val == '#' 

    return core_map

def build_flat_plane_coord(x, y, n=None):
    if not n:
        preamble = [int(i) for i in '0'*(DIMENSIONS-2)]
    else:
        preamble = list(n)
    preamble.extend([x, y])
    return tuple(preamble)

def get_all_locations(core_map):
    lim = -list(core_map.keys())[0][-3]
    n_dim  = list(range(-(lim), +(lim+1)))
    n_dims = list(itertools.product(n_dim, repeat=DIMENSIONS-2))
    
    x_co = set([i[-1] for i in core_map.keys()])
    y_co = set([i[-2] for i in core_map.keys()])

    result = []
    for n in n_dims:
        for x in sorted(x_co):
            for y in sorted(y_co):
                result.append(build_flat_plane_coord(x, y, n))

    return result

def render_map(core_map):
    '''
    Renders the central slice of thing.
    This function only works on the example. Its broken for the actual puzzle input.
    I dont know why. I dont care to find out.
    '''
    x_co = set([i[-2] for i in core_map.keys()])
    y_co = set([i[-1] for i in core_map.keys()])
    
    for x in sorted(x_co):
        for y in sorted(y_co):
            if core_map[build_flat_plane_coord(x, y)]:
                print('█', end=' ')
            else:
                print('░', end=' ')
        print()


problem_input = [
    '#.#.##.#',
    '#.####.#',
    '...##...',
    '#####.##',
    '#....###',
    '##..##..',
    '#..####.',
    '#...#.#.',
]

core_map = import_input(problem_input, 6)
print(len(core_map.keys()))

prev = core_map
# render_map(prev)
print('.')
for _ in range(6):

    updated_map = {}
    for i in get_all_locations(prev):
        updated_map[i] = update_state(i, prev)
    prev = updated_map

    # render_map(prev)
    print('.')

final_fucking_result = [i for i in get_all_locations(prev) if prev[i] is True]
print(len(final_fucking_result))
