import binary_parser

with open("Day_5/input_5.txt", 'r') as f:
    data = f.readlines()

seat_ids = []
for s in data:
    seat_loc = binary_parser.parse_seat(s.strip())
    seat_id = binary_parser.get_seat_id(seat_loc)
    seat_ids.append(seat_id)

prev = False
for i in sorted(seat_ids):
    if prev:
        if i - 1 != prev:
            print("Missing!", i - 1)

    prev = i