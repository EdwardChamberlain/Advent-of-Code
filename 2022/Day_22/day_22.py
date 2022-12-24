import sys
import os
import re
import numpy as np
import day_22_2

DIM = 49
PORTALS = {
    (0, 'N'): lambda y, x: (5,  (x, 0), 'E'),
    (0, 'E'): lambda y, x: (1,  (y, 0), 'E'),
    (0, 'S'): lambda y, x: (2,  (0,  x), 'S'),
    (0, 'W'): lambda y, x: (3,  (DIM-y, 0), 'E'),

    (1, 'N'): lambda y, x: (5,  (DIM,  DIM-x), 'N'),
    (1, 'E'): lambda y, x: (4,  (DIM-y,  DIM), 'W'),
    (1, 'S'): lambda y, x: (2,  (x,  DIM), 'W'),
    (1, 'W'): lambda y, x: (0,  (y,  DIM), 'W'),

    (2, 'N'): lambda y, x: (0,  (DIM,  x), 'N'),
    (2, 'E'): lambda y, x: (1,  (DIM,  y), 'N'),
    (2, 'S'): lambda y, x: (4,  (0,  x), 'S'),
    (2, 'W'): lambda y, x: (3,  (0,  y), 'S'),

    (3, 'N'): lambda y, x: (2,  (x,  0), 'E'),
    (3, 'E'): lambda y, x: (4,  (y,  0), 'E'),
    (3, 'S'): lambda y, x: (5,  (0,  x), 'S'),
    (3, 'W'): lambda y, x: (0,  (DIM-y,  0), 'W'),

    (4, 'N'): lambda y, x: (2,  (DIM,  x), 'N'),
    (4, 'E'): lambda y, x: (1,  (DIM-y,  DIM), 'W'),
    (4, 'S'): lambda y, x: (5,  (y,  DIM), 'W'),
    (4, 'W'): lambda y, x: (4,  (y,  DIM), 'W'),

    (5, 'N'): lambda y, x: (3,  (DIM,  x), 'N'),
    (5, 'E'): lambda y, x: (4,  (DIM,  y), 'N'),
    (5, 'S'): lambda y, x: (1,  (0,  DIM-x), 'N'),
    (5, 'W'): lambda y, x: (0,  (0,  y), 'S'),
}


def get_data():
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
        data = data.split('\n\n')
    
    space = parse_space(data[0])
    directions = parse_directions(data[1])

    return space, directions


def make_lists_same_length(input_list, padder=' '):
    max_len = len(max(input_list, key=len))
    return [s + [padder] * (max_len - len(s)) for s in input_list]


def parse_space(space):
    space = [list(s) for s in space.split('\n')]
    space = make_lists_same_length(space)
        
    space = np.array(space)
    return space


def parse_directions(directions):
    return re.findall(r'\d+|\D', directions)


def print_space(space):
    for s in space:
        print(''.join(s))


headings = ['E', 'S', 'W', 'N']
def rotate_heading(current_heading, direction):
    current_heading = headings.index(current_heading)

    delta = 1 if direction == 'R' else -1
    current_heading = headings[(current_heading + delta) % 4]

    return current_heading


def move_position(current_position, current_heading):
    if current_heading == 'N':
        current_position = (current_position[0] - 1, current_position[1])

    elif current_heading == 'E':
        current_position = (current_position[0], current_position[1] + 1)

    elif current_heading == 'S':
        current_position = (current_position[0] + 1, current_position[1])

    elif current_heading == 'W':
        current_position = (current_position[0], current_position[1] - 1)

    return current_position

def move(space, start_position, heading):
    new_position = move_position(start_position, heading)
    valid_spaces = ['.', '#']

    try:
        assert space[new_position] in valid_spaces
    except:
        match heading:
            case 'N':
                col = space[:, new_position[1]]
                index = np.where((col == '.') | (col == '#'))[0][-1]
                new_position = (index, new_position[1])

            case 'S':
                col = space[:, new_position[1]]
                index = np.where((col == '.') | (col == '#'))[0][0]
                new_position = (index, new_position[1])

            case 'E':
                row = space[new_position[0], :]
                index = np.where((row == '.') | (row == '#'))[0][0]
                new_position = (new_position[0], index)

            case 'W':
                row = space[new_position[0], :]
                index = np.where((row == '.') | (row == '#'))[0][-1]
                new_position = (new_position[0], index)

    
    if space[new_position] == '#':
        return start_position

    return new_position

def move3d(faces, start_face, start_position, heading):
    new_position = move_position(start_position, heading)
    new_face = start_face
    new_heading = heading

    valid_spaces = ['.', '#']

    try:
        assert faces[start_face][new_position] in valid_spaces
        assert -1 not in new_position
    except:
        new_face, new_position, new_heading = PORTALS[(start_face, heading)](*start_position)

    
    if faces[new_face][new_position] == '#':
        return start_face, start_position, heading

    return new_face, new_position, new_heading


def get_start_position(space):
    return np.where(space[0] == '.')[0][0]


def pt_1(space, directions):
    current_position = (0, get_start_position(space))
    current_heading = 'E'

    for direction in directions:
        if direction in ['L', 'R']:
            current_heading = rotate_heading(current_heading, direction)

        else:
            for _ in range(int(direction)):
                current_position = move(space, current_position, current_heading)

    facing_value = headings.index(current_heading)
    result = ((current_position[0] + 1) * 1000) + (4 * (current_position[1] + 1)) + facing_value
    print('result', result)


def extract_faces(space, face_size):
    faces = []
    for r in range(0, len(space), face_size):
        rows = space[r:r+face_size]

        row = rows[0]
        occupied = np.where((row == '.') | (row == '#'))[0]
        start = occupied[0]
        end = occupied[-1]

        for c in range(start, end + 1, face_size):
            face = rows[:, c : c+face_size]
            faces.append(face)

    return faces


def pt_2(space, directions):
    # print_space(space)
    # print()

    faces = extract_faces(space, 50)

    current_face = 0
    current_position = (0, 0)
    current_heading = 'E'

    extras = {
        0: 0,
        1: 0,
        2: 50,
        3: 100,
        4: 100,
        5: 150,
    }


    instructions = []
    for direction in directions:
        instructions.append(direction)
        print('direction', direction)
        if direction in ['L', 'R']:
            current_heading = rotate_heading(current_heading, direction)

        else:
            for _ in range(int(direction)):
                current_face, current_position, current_heading = move3d(faces, current_face, current_position, current_heading)
            
            row = current_position[0] + 1 + extras[current_face]
            col = current_position[1] + 1
            heading = headings.index(current_heading)
            result = 1000 * row + 4 * col + heading

            day_22_2.INSTRUCTIONS = instructions
            print(day_22_2.INSTRUCTIONS)
            result_alt = day_22_2.part_two()
            print()
            print('result alt', result_alt)
            print('result', result)
            print(row, col, heading)

            if result_alt != result:
                exit()

        print()



if __name__ == '__main__':
    space, directions = get_data()
    # pt_1(space, directions)
    pt_2(space, directions)