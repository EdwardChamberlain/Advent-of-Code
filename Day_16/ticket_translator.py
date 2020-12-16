def validate(value, requirement):
    for n in requirement:
        if int(n[0]) <= value <= int(n[1]):
            return True
    return False

def is_valid_value(value, requirement):
    for i in requirement.values():
        if validate(value, i):
            return True
    return False

def is_valid_ticket(ticket, requirement):
    validity = [is_valid_value(v, requirement) for v in ticket]
    return all(validity)

def get_possible_keys(tickets, requirements):
    possibles = {}
    for i in range(len(tickets[0])):
        result = []
        col = [p[i] for p in tickets]
        for name, rule in requirements.items():
            truthy = [validate(i, rule) for i in col]
            if all(truthy):
                # print(i, name)
                result.append(name)

        possibles[i] = result
    return possibles

def solve_possibles(possibles):
    mappings = {}
    for k, v in sorted(possibles.items(), key=lambda u: len(u[1])):
        result = list(set(v) - set(mappings.keys()))
        mappings[result[0]] = k
    return mappings

def get_ticket_mappings(tickets, requirements):
    possibles = get_possible_keys(tickets, requirements)
    mappings = solve_possibles(possibles)
    return mappings