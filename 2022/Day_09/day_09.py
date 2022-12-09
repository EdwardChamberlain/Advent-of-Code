import sys
import os


def get_vector(x, y):
    return unit((x[0] - y[0], x[1] - y[1]))
    

def unit(x):
    a, b = x
    return (make_1(a), make_1(b))


def make_1(x: int) -> int:
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def update_tail(head, tail):
    if is_touching(head, tail):
        return tail

    vect = get_vector(head, tail)
    tail = (tail[0] + vect[0], tail[1] + vect[1])
    return tail
    

def is_touching(head, tail) -> bool:
    return head[0] - 1 <= tail[0] <= head[0] + 1 and head[1] - 1 <= tail[1] <= head[1] + 1


def move_head(head, direction):
    x, y = head

    if direction == 'U':
        y += 1
    if direction == 'D':
        y -= 1
    if direction == 'L':
        x -= 1
    if direction == 'R':
        x += 1

    return (x, y)


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 
    data = [d.split(' ') for d in data]

head = (0, 0)
tail = (0, 0)

tail_positions = []
for cmd in data:
    direction, repeats = cmd
    repeats = int(repeats)
    print(direction)
    
    for _ in range(repeats):
        head = move_head(head, direction)
        tail = update_tail(head, tail)
        # print(head, tail)
        tail_positions.append(tail)

print(len(set(tail_positions)))

