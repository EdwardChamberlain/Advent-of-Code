import itertools


def mask_value(value, mask):
    binary = list(f'{int(value):036b}')
    for i, _ in enumerate(binary):
        if mask[i] == 'X':
            continue
        else:
            binary[i] = mask[i]
    return int(''.join(binary), 2)

def apply_masking(value, mask):
    binary = list(f'{int(value):036b}')
    for i, _ in enumerate(binary):
        if mask[i] == 'X':
            binary[i] = 'X'
        else:
            binary[i] = str(int(binary[i]) or int(mask[i]))
    return ''.join(binary)

def get_all_addresses(address):
    result = []
    number_X = len([i for i in address if i == 'X'])
    for i, v in enumerate(itertools.product(range(2), repeat=number_X)):
        temp = list(address)
        # print(temp)

        for n in v:
            temp[temp.index('X')] = str(n)

        result.append(int(''.join(temp), 2))
    return result