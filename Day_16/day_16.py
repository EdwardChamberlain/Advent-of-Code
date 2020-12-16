import re
import ticket_translator
from math import prod


# ~~~~~~~~~~~ Get Data ~~~~~~~~~~~

with open("Day_16/input_16.txt", 'r') as f:
    data = [i.split('\n') for i in f.read().split('\n\n')]

your_ticket = [int(i) for i in data[1][1].split(',')]
nearby_tickets = [[int(n) for n in i.split(',')] for i in data[2][1:]]
requirements = {}
for i in data[0]:
    req_name = re.search(r'(.+):', i)[1]
    req = re.findall(r'(\d+)-(\d+)', i)
    requirements[req_name] = ([int(i) for i in req[0]], [int(i) for i in req[1]])


# ~~~~~~~~~~~ Pt 1 ~~~~~~~~~~~

invalid_values = []
for t in nearby_tickets:
    for n in t:
        invalid_values.append(ticket_translator.get_invalid_values(n, requirements))

print(f"Pt 1: {sum([i for i in invalid_values if i is not None])}")


# ~~~~~~~~~~~ Pt 2 ~~~~~~~~~~~

valid_nearby_tickets = [i for i in nearby_tickets if ticket_translator.is_valid_ticket(i, requirements)]
mappings = ticket_translator.get_ticket_mappings(valid_nearby_tickets, requirements)
indexs = [v for k, v in mappings.items() if k.startswith('departure ')]

result = prod([your_ticket[i] for i in indexs])

print(f"Pt 2: {result}")
