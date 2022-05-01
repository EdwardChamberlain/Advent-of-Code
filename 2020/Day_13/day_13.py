import math
import string
from sympy.ntheory.modular import crt 

with open("Day_13/input_13.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

buses = [int(i) for i in data[1].split(',') if i != 'x']
START_TIME = int(data[0])

results = {}
for i in buses:
    next_time = math.ceil(START_TIME/i)
    results[i] = next_time * i

earliest_bus = (min(results, key=results.get))

time_to_wait = results[earliest_bus] - START_TIME
result = time_to_wait * earliest_bus

print(f"Pt 1: {result}")

# ~~~~~~~~~~ Pt 2 ~~~~~~~~~~

deltas = {int(b):i for i, b in enumerate(data[1].split(',')) if b != 'x'}

m = [i for i in deltas]
v = [m[i] - d for i, d in enumerate(deltas.values())]
v[0] = 0

result = crt(m, v)
print(f"Pt 2: {result[0]}")