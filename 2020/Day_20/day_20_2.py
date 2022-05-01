from sqlite3 import Row
from tkinter import Y

from collections import Counter


with open("2020/Day_20/input_20.txt", 'r') as f:
    data = [i.split('\n') for i in f.read().split('\n\n')]

d = [
    '.##...#..#',
    '.#.#.#...#',
    '.......###',
    '.....##.#.',
    '#...#.....',
    '##...#...#',
    '#.#.#....#',
    '##..##....',
    '.....#.#..',
    '##.#......',
]

d2 = [
    '###...#..#',
    '.#.#.#...#',
    '.......###',
    '.....##.#.',
    '#...#.....',
    '##...#...#',
    '#.#.#....#',
    '##..##....',
    '.....#.#..',
    '##.#......',
]

class Jigsaw_Piece:
    def __init__(self, id, data):
        self.data = [
            [
                True if i == '#' else False
                for i in row    
            ]
            for row in d
        ]

    def edges(self):
        edges = (
            self.data[0],
            self.data[-1],
            [i[0]  for i in self.data],
            [i[-1] for i in self.data],
        )
        return edges

    def render(self):
        for row in self.data:
            for p in row:
                if p:
                    print('■', end='')
                else:
                    print('□', end='')
            print()


mjp = Jigsaw_Piece(0, d)
mjp2 = Jigsaw_Piece(0, d2)

mjp.render()
for i in mjp.edges():
    print(i)

def compare_edges(a, b):
    compare = set(a.edges())&set(b.edges())
    print(compare)

print(type(mjp.edges()))

print(len(compare_edges(mjp, mjp)))

# frames = []
# for i in data:
#     frame_id = i[0].split()[1][:-1]
#     frame_data = [[p == '#' for p in n] for n in i[1:]]
#     frames.append(Jigsaw_Piece(frame_id, frame_data))

