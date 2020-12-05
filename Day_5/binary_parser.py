import math

def parse_seat(seat_code):
    row = bin_parse(seat_code[:7])
    col = bin_parse(seat_code[7:])

    return (row, col)

def bin_parse(input_string):
    rows = [i for i in range(2**len(input_string))]

    for i in input_string:
        if (i == 'F') or (i == 'L'):
            rows = rows[:(math.floor(len(rows)/2))]
        else:
            rows = rows[(math.floor(len(rows)/2)):]

    return rows[0]

def get_seat_id(seat_loc):
    return seat_loc[0] * 8 + seat_loc[1]
