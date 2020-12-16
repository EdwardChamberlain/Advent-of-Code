import re
import ticket_translator
from math import prod


tracker = []

def is_valid_value(value, requirement):
    for i in requirements.values():
        for n in i:
            if n[0] <= value <= n[1]:
                return True
    tracker.append(value)
    return False

def is_valid_ticket(ticket, requirement):
    validity = [is_valid_value(v, requirements) for v in ticket]
    return all(validity)


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

for t in nearby_tickets:
    is_valid_ticket(t, requirements)

print(f"Pt 1: {sum(tracker)}")


# ~~~~~~~~~~~ Pt 2 ~~~~~~~~~~~

valid_nearby_tickets = [i for i in nearby_tickets if ticket_translator.is_valid_ticket(i, requirements)]
mappings = ticket_translator.get_ticket_mappings(valid_nearby_tickets, requirements)
indexs = [v for k, v in mappings.items() if k.startswith('departure ')]

result = prod([your_ticket[i] for i in indexs])

print(f"Pt 2: {result}")
