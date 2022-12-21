import sys
import os
import operator
import sympy


opperators = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.truediv,
}


def get_data():
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
        data = data.split('\n')
        data = [d.split(': ') for d in data]
    return data


def get_monkeys(data):
    return {d[0]: d[1].split(' ') for d in data}


def solve_monkey(monkey_name, monkeys, symbolic=False):
    if monkey_name == 'humn' and symbolic:
        return sympy.symbols('x')

    monkey = monkeys[monkey_name]

    if len(monkey) == 1:
        return int(monkey[0])

    else:
        return opperators[monkey[1]](
            solve_monkey(monkey[0], monkeys, symbolic),
            solve_monkey(monkey[2], monkeys, symbolic),
        )


def pt_1(data):
    monkeys = get_monkeys(data)

    result = solve_monkey('root', monkeys)
    print(result)


def pt_2(data):
    monkeys = get_monkeys(data)

    root_monkey = monkeys['root']
    monkey_a = root_monkey[0]
    monkey_b = root_monkey[2]

    monkey_a = solve_monkey(monkey_a, monkeys, symbolic=True)
    monkey_b = solve_monkey(monkey_b, monkeys, symbolic=True)

    result = sympy.solvers.solve(monkey_a - monkey_b, sympy.symbols('x'))
    print(result[0])


if __name__ == '__main__':
    data = get_data()

    pt_1(data)
    pt_2(data)
