import sys
import os
import operator


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = [d.split(',') for d in data]
    data = [list(map(int, d)) for d in data]


def add_vector(a, b):
    return list(map(operator.add, a, b))


neighbours = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]


if __name__ == '__main__':
    SAs = []
    for d in data:
        SA = 6
        for n in neighbours:
            neighbour = add_vector(d, n)
            if neighbour in data:
                SA -= 1

        SAs.append(SA)

    print(sum(SAs))