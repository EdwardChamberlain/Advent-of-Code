import collections


def get_connected_coords(coord, data):
    x, y = coord
    result = (
        (x + 1, y), # Below
        (x - 1, y), # Above
        (x, y + 1), # Right
        (x, y - 1), # Left
        (x + 1, y + 1), # up-right
        (x + 1, y - 1), # up-left
        (x - 1, y + 1), # down-right
        (x - 1, y - 1), # down-left
    )

    result = [i for i in result if not i[0] < 0 and not i[1] < 0]
    result = [i for i in result if not i[0] >= len(data) and not i[1] >= len(data[1])]
    return result

def update_seat(seat, neighbours):
    if seat == 'L' and neighbours['#'] == 0:
        return '#'
    elif seat == '#' and neighbours['#'] >= 4:
        return 'L'
    else:
        return seat

def seat_state_update(x, y, data):
    target_seat = data[x][y]

    neighbours_coords = get_connected_coords((x, y), data)

    neighbours = [data[i[0]][i[1]] for i in neighbours_coords]
    neighbours_col = collections.Counter(neighbours)

    return update_seat(target_seat, neighbours_col)

def calc_new_seat_plan(data):
    return [[seat_state_update(x, y, data) for y, y_data in enumerate(x_data)] for x, x_data in enumerate(data)]

def seats_in_use(seating_plan):
    acc = 0
    for x in seating_plan:
        for y in x:
            if y == '#':
                acc += 1
    return acc
