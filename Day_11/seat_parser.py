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

def seat_state_update(x, y, data):
    target_seat = data[x][y]

    neighbours_coords = get_connected_coords((x, y), data)

    neighbours = [data[i[0]][i[1]] for i in neighbours_coords]
    neighbours_col = collections.Counter(neighbours)

    return update_seat(target_seat, neighbours_col)

def update_seat(seat, neighbours):
    if seat == 'L' and neighbours['#'] == 0:
        return '#'
    elif seat == '#' and neighbours['#'] >= 4:
        return 'L'
    else:
        return seat

def seats_in_use(seating_plan):
    acc = 0
    for x in seating_plan:
        for y in x:
            if y == '#':
                acc += 1
    return acc

def calc_new_seat_plan(data):
    return [[seat_state_update(x, y, data) for y, y_data in enumerate(x_data)] for x, x_data in enumerate(data)]

def add_vect(a, b):
    return (a[0] + b[0], a[1] + b[1])

def is_valid_location(coord, data):
    return 0 <= coord[0] < len(data) and 0 <= coord[1] < len(data[0])

def get_seat_in_direction(start, vect, data):
    while True:
        start = add_vect(start, vect)
        if not is_valid_location(start, data):
            break
        x, y = start
        if data[x][y] == 'L' or data[x][y] == '#':
            return x, y
    return None

def get_connected_seats(coord, data):
    vects = (
        (1, 0), # Below
        (-1, 0), # Above

        (0, 1), # Right
        (0, -1), # Left

        (1, 1), # up-right
        (1, -1), # up-left
        (-1, 1), # down-right
        (-1, -1), # down-left
    )
    result = [get_seat_in_direction(coord, v, data) for v in vects if get_seat_in_direction(coord, v, data) is not None]
    return collections.Counter([data[i[0]][i[1]] for i in result])

def update_seat2(seat, neighbours):
    if seat == 'L' and neighbours['#'] == 0:
        return '#'
    elif seat == '#' and neighbours['#'] >= 5:
        return 'L'
    else:
        return seat

def seat_state_update2(x, y, data):
    target_seat = data[x][y]
    return update_seat2(target_seat, get_connected_seats((x, y), data))

def calc_new_seat_plan2(data):
    return [[seat_state_update2(x, y, data) for y, y_data in enumerate(x_data)] for x, x_data in enumerate(data)]
