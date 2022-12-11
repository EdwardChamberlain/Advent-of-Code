import sys
import os
import copy


class Monkey:
    def __init__(self, objects: list[int], operation, check, true_target, false_target):
        self.objects = objects
        self.check = check
        self.operation = operation
        self.true_target = true_target
        self.false_target = false_target
        self.inspections = 0
    
    def __repr__(self) -> str:
        return f"Monkey: {self.inspections:>8} :: {self.objects}"

    def update_object(self, x: int):
        global SCALER
        return self.operation(x) % SCALER # // 3

    def run_test(self, x: int):
        return self.check(x)

    def process_object(self, x: int): 
        x = self.update_object(x)
        self.inspections += 1
        if self.run_test(x):
            return self.true_target, x
        else:
            return self.false_target, x

    def process_all_objects(self):
        results = [
            self.process_object(o)
            for o in self.objects
        ]
        self.objects = []
        return results

    def add_object(self, x: int):
        self.objects.append(x)


ops = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
}


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n\n')
    data = [d.split('\n') for d in data]


monkeys = []
SCALER = 1
for monkey in data:
    items = monkey[1].split(': ')[-1].split(', ')
    items = list(map(int, items))

    operation = monkey[2].split(': ')[-1]
    operation = operation.split(' ')
    a = operation[-3]
    b = operation[-1]
    op = operation[-2]
    operation_func = lambda x, a=a, b=b, op=op: ops[op](
        x if a == 'old' else int(a),
        x if b == 'old' else int(b),
    )

    test = monkey[3].split(': ')[-1]
    test = int(test.split(' ')[-1])
    SCALER *= test
    test_func = lambda x, test=test: x % test == 0

    true_target = int(monkey[4].split(' ')[-1])
    false_target = int(monkey[5].split(' ')[-1])

    monkeys.append(
        Monkey(items, operation_func, test_func, true_target, false_target)
    )


def run_inspections(cycles, monkeys):
    for n in range(cycles):
        for monkey in monkeys:
            result = monkey.process_all_objects()

            for m, i in result:
                monkeys[m].add_object(i)

run_inspections(10000, monkeys)
inspections = [monkey.inspections for monkey in monkeys]
inspections = sorted(inspections, reverse=True)
print(inspections[0] * inspections[1])
