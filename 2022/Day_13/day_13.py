import sys
import os
import ast
import functools


def compare_int_int(l: int, r: int) -> bool:
    if l < r:
        return True
    elif l == r:
        return None
    else:
        return False


def compare_lists(left: list, right: list) -> bool:
    for l, r in zip(left, right):

        if isinstance(l, int) and isinstance(r, int):
            result = compare_int_int(l, r)
            if result is None:
                continue
            else:
                return result

        elif isinstance(l, list) and isinstance(r, list):
            result = compare_lists(l, r)
            if result is None:
                continue
            else:
                return result

        elif isinstance(l, int) and isinstance(r, list) or isinstance(l, list) and isinstance(r, int):
            if isinstance(l, int): l = [l]
            if isinstance(r, int): r = [r]

            result = compare_lists(l, r)
            if result is None:
                continue
            else:
                return result

        else:
            raise TypeError('Unknown types')
        
    else:
        if len(left) > len(right):
            return False
        elif len(left) == len(right):
            return None
        else:
            return True


def key_lists(left, right) -> int:
    if compare_lists(left, right):
        return -1
    else:
        return 1


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    raw_data = f.read()

# Pt 1
data = raw_data.split('\n\n')
data = [d.split('\n') for d in data]

correct = []
for i, d in enumerate(data):
    left, right = d
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)

    if compare_lists(left, right):
        correct.append(i+1)

print(sum(correct))


# Pt 2
data = raw_data.split('\n')
data = [d for d in data if not d == '']
data.append('[[2]]')
data.append('[[6]]')
data = [ast.literal_eval(d) for d in data]

sorted_data = sorted(data, key=functools.cmp_to_key(key_lists))

i1 = sorted_data.index([[2]]) + 1
i2 = sorted_data.index([[6]]) + 1

print(i1 * i2)
