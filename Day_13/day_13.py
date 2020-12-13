import math

with open("Day_13/input_13.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]
data[1] = [int(i) for i in data[1].split(',') if i != 'x']

START_TIME = int(data[0])

results = {}
for i in data[1]:
    next_time = math.ceil(START_TIME/i)
    results[i] = next_time * i

earliest_bus = (min(results, key=results.get))

time_to_wait = results[earliest_bus] - START_TIME
result = time_to_wait * earliest_bus

print(f"Pt 1: {result}")