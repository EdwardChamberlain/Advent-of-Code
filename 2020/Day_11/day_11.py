import seat_parser
import collections

with open("Day_11/input_11.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

seat_plan = data

loop_counter = 0
prev_seats = 50

while seat_parser.seats_in_use(seat_plan) != prev_seats:
    prev_seats = seat_parser.seats_in_use(seat_plan)
    seat_plan = seat_parser.calc_new_seat_plan(seat_plan)
    loop_counter += 1

print(f"Pt 1: Loops Taken: {loop_counter}")
print(f"Pt 1: Total seats in use: {prev_seats}")

# ~~~~~~~~~~~~~~~~~ Pt 2 ~~~~~~~~~~~~~~~~~~~~~~

seat_plan = data

loop_counter = 0
prev_seats = 50

while seat_parser.seats_in_use(seat_plan) != prev_seats:
    prev_seats = seat_parser.seats_in_use(seat_plan)
    seat_plan = seat_parser.calc_new_seat_plan2(seat_plan)
    loop_counter += 1

print(f"Pt 2: Loops Taken: {loop_counter}")
print(f"Pt 2: Total seats in use: {prev_seats}")