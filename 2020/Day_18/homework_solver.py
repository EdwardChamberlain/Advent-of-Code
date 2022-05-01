import re


def solve(string):
    string = resolve_bracket(string, solver=solve)
    return accumulate(string)

def solve2(string):
    string = resolve_bracket(string, solver=solve2)

    if '*' in string:
        string = prioritise_add(string)
        string = resolve_bracket(string, solve2)

    return accumulate(string)

def op(acc, op_tuple):
    op, value = op_tuple
    if op == '+':
        return acc + int(value)
    elif op == '*':
        return acc * int(value)

def parenthetic_contents(string):
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])

def resolve_bracket(string, solver):
    brackets = [i[1] for i in parenthetic_contents(string) if i[0] == 0]
    for b in brackets:
        string = string.replace(f"({b})", str(solver(b)), 1)
    return string

def prioritise_add(string):
    return re.sub(r'(?:\d+ \+ )+\d+', lambda m: f"({m[0]})", string)

def accumulate(string):
    accumulator = int(string.split(' ')[0].strip('('))
    for i in re.findall(r'(\+|\*) (\d+)', string):
        accumulator = op(accumulator, i)
    return accumulator
