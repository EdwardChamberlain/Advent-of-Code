import sys
import os
import collections
import cProfile
import itertools


def get_data():
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
        data = data.split('\n')
    return data


def get_elf_positions(data):
    elves = set()
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell == '#':
                elves.add(complex(r, c))
    return elves


def has_any_neighbour(elves, elf):
    for n in get_neighbours(elf):
        if n in elves:
            return True
    return False


def get_neighbours(xy):
    vectors = [
        0 + 1j, 0 - 1j, 1 + 0j, -1 + 0j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j,
    ]

    for v in vectors:
        yield xy + v

def get_directional_neighbours(xy, direction):
    vectors = {
        'N': [-1 +0j, -1 +1j, -1 -1j],
        'S': [+1 +0j, +1 +1j, +1 -1j],
        'W': [+0 -1j, +1 -1j, -1 -1j],
        'E': [+0 +1j, +1 +1j, -1 +1j],
    }

    for v in vectors[direction]:
        yield xy + v

def elf_in_direction(xy, direction, elves):
    for n in get_directional_neighbours(xy, direction):
        if n in elves:
            return True
    return False


def get_unqiue_spaces(proposals):
    unique_spaces = collections.Counter(proposals.values())
    unique_spaces = set(k for k, v in unique_spaces.items() if v == 1)

    return unique_spaces


def generate_proposals(elves, instructions, return_moves=False):
    proposals = {}
    moves = 0
    for elf in elves:
        if has_any_neighbour(elves, elf):
            for direction in instructions:
                if not elf_in_direction(elf, direction, elves):
                    proposals[elf] = next(get_directional_neighbours(elf, direction))
                    moves += 1
                    break
            else:
                proposals[elf] = elf
        else:
            proposals[elf] = elf

    if return_moves:
        return proposals, moves
    else:
        return proposals


def update_elf_positions(proposals, unique_spaces):
    return set(
        v if v in unique_spaces else k
        for k, v in proposals.items()
    )


def get_bounding_box_area(elves):
    x = [e.imag for e in elves]
    y = [e.real for e in elves]

    width = max(x) - min(x) + 1
    height = max(y) - min(y) + 1
    area = width * height

    return area


INITIAL_INSTRUCTIONS = [
    'N',
    'S',
    'W',
    'E',
]


def cycle_instructions(instructions):
    x = instructions.pop(0)
    instructions.append(x)
    return instructions


def pt_1(data, cycles=10):
    elves = get_elf_positions(data)

    instructions = INITIAL_INSTRUCTIONS.copy()
    for _ in range(cycles):
        proposals = generate_proposals(elves, instructions)
        unique_spaces = get_unqiue_spaces(proposals)

        elves = update_elf_positions(proposals, unique_spaces)
        instructions = cycle_instructions(instructions)

    area = get_bounding_box_area(elves)
    free_space = area - len(elves)
    print('free space', free_space)


def pt_2(data):
    elves = get_elf_positions(data)

    instructions = INITIAL_INSTRUCTIONS.copy()
    for n in itertools.count():
        print('round', n + 1, end='\r')
        proposals, moves = generate_proposals(elves, instructions, return_moves=True)

        if moves == 0:
            print('\nno moves after', n + 1, 'rounds')
            break

        unique_spaces = get_unqiue_spaces(proposals)

        elves = update_elf_positions(proposals, unique_spaces)
        instructions = cycle_instructions(instructions)


if __name__ == "__main__":
    data = get_data()

    pt_1(data, cycles=10)
    pt_2(data)

    # cProfile.run('pt_1(data, cycles=10)')
    # cProfile.run('pt_2(data)')
