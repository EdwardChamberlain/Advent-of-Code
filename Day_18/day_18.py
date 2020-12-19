import re

def op(acc, op_tuple):
    op, value = op_tuple
    if op == '+':
        return acc + int(value)
    elif op == '*':
        return acc * int(value)
    else:
        raise NotImplementedError(op_tuple)

def parenthetic_contents(string):
    """Generate parenthesized contents in string as pairs (level, contents)."""
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])

def solve(string):
    brackets = list(parenthetic_contents(string))
    brackets = [i[1] for i in brackets if i[0] == 0]

    for b in brackets:
        string = string.replace(f"({b})", str(solve(b)))

    start = int(string.split(' ')[0])
    ops = re.findall(r'(\+|\*) (\d+)', string)
    accumulator = start
    for i in ops:
        accumulator = op(accumulator, i)

    return accumulator

with open("Day_18/input_18.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

result = [solve(i) for i in data]

print(f"Pt 1: {sum(result)}")