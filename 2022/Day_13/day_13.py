import sys
import os
import ast


def compare_int_int(l: int, r: int) -> bool:
    if l < r:
        return True
    elif l == r:
        return None
    else:
        return False


def compare_lists(left: list, right: list) -> bool:
    for l, r in zip(left, right):
        print('Compare: ', l, 'vs', r)

        if isinstance(l, int) and isinstance(r, int):
            print('both ints')
            result = compare_int_int(l, r)
            print(result)
            print()
            if result is None:
                continue
            else:
                return result

        elif isinstance(l, list) and isinstance(r, list):
            print('both lists')

            result = compare_lists(l, r)
            if result is None:
                continue
            else:
                return result

        elif isinstance(l, int) and isinstance(r, list) or isinstance(l, list) and isinstance(r, int):
            print('one list, one int')

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
        print("List exhasuted")
        if len(left) > len(right):
            print("Left longer")
            return False
        elif len(left) == len(right):
            return None
        else:
            return True



with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()

# Pt 1
data = data.split('\n\n')
data = [d.split('\n') for d in data]

correct = []
for i, d in enumerate(data):
    print()
    print(f"=== Pair {i+1} ===")

    left, right = d
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)

    print(f"Compare {left} vs {right}")

    if compare_lists(left, right):
        print("Correct")
        correct.append(i+1)
    else:
        print("Incorrect")

print(correct)
print(sum(correct))