import sys
import os
import operator
import numpy as np
import functools
np.set_printoptions(threshold=sys.maxsize)


def get_data():
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = [d.split(',') for d in data]
        data = [list(map(int, d)) for d in data]
    return data


def add_vector(a, b):
    return list(map(operator.add, a, b))


def get_neighbours(d, space=None):
    neighbours = [
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0),
    ]

    if space is not None:
        for n in neighbours:
            n = add_vector(d, n)
            if -1 not in n and n[0] < space.shape[0] and n[1] < space.shape[1] and n[2] < space.shape[2]:
                yield n

    else:
        for n in neighbours:
            yield add_vector(d, n)


def bfs(p, space):
    visited = []
    queue = []

    queue.append(p)

    while queue:
        s = queue.pop()

        for n in get_neighbours(s, space):
            if n in visited:
                continue

            else:
                if space[n[0], n[1], n[2]] == '.':
                    queue.append(n)
                    visited.append(n)

    return visited
    

def pt_1(data):
    SAs = []
    for d in data:
        SA = 6
        for n in get_neighbours(d):
            if n in data:
                SA -= 1
        SAs.append(SA)

    return sum(SAs)


def pt_2(data):
    points = np.array(data)
    x_max = max(points[:, 0]) + 2
    y_max = max(points[:, 1]) + 2
    z_max = max(points[:, 2]) + 2
    space = np.full((x_max, y_max, z_max), '.')

    for d in data:
        space[d[0], d[1], d[2]] = '#'

    external_faces = bfs([0, 0, 0], space)
    # for ef in external_faces:
    #     space[ef[0], ef[1], ef[2]] = 'O'

    SAs = []
    for d in data:
        surface_area = 6
        for n in get_neighbours(d):
            if n in data:
                surface_area -= 1

            elif n not in external_faces:
                surface_area -= 1 

        SAs.append(surface_area)

    return sum(SAs)


if __name__ == '__main__':
    data = get_data()
    print(pt_1(data))
    print(pt_2(data))