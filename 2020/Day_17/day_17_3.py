import collections
import itertools

def compute(initial_state, DIMENSIONS = 3):
    ADJACENT_VECTORS = list(itertools.product(range(-1, 2), repeat=DIMENSIONS))
    ADJACENT_VECTORS.remove(tuple((0 for _ in range(DIMENSIONS))))

    cubes = [
        (x, y, *[0]*(DIMENSIONS-2))
        for y, row in enumerate(initial_state)
        for x, cell in enumerate(row) 
        if cell == '#'
    ]

    for _ in range(6):
        marked = collections.Counter()
        for coord in cubes:
            adjacent = [
                tuple(a + b for a, b in zip(coord, vector))
                for vector in ADJACENT_VECTORS
            ]
            for i in adjacent:
                marked[i] += 1

        activated = [
            k
            for k in cubes
            if marked[k] == 2
        ]
        for k, v in marked.items():
            if v == 3:
                activated.append(k)
        cubes = activated

    print(f"Dimensions: {DIMENSIONS}:\n   Activated Cubes: {len(cubes)}")

if __name__ == '__main__':
    initial_state = [
        '#.#.##.#',
        '#.####.#',
        '...##...',
        '#####.##',
        '#....###',
        '##..##..',
        '#..####.',
        '#...#.#.',
    ]

    compute(initial_state, DIMENSIONS=3)
    compute(initial_state, DIMENSIONS=4)