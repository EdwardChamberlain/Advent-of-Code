with open('inputs/day_3.txt') as f:
    data = f.readlines()
    data = [d.strip() for d in data]

rotated_data = [
    [
        i[n]
        for i in data
    ]
    for n in range(len(data[0]))
]

gama_bits = [
    '0' if i.count('0') > i.count('1') else '1'
    for i in rotated_data
]

epsilon_bits = [
    '1' if i.count('0') > i.count('1') else '0'
    for i in rotated_data
]

gama = int(''.join(gama_bits), 2)
epsilon = int(''.join(epsilon_bits), 2)

print(gama*epsilon)

###### PART 2 ######
working_data = data.copy()
for b in range(len(data[0])):
    bytes = [
        i[b]
        for i in data
    ]

    search_bit = '1' if bytes.count('1') >= bytes.count('0') else '0'

    working_data = [
        n
        for n in working_data
        if n[b] == search_bit
    ]

    if len(working_data) == 1:
        break

ox_gen_rat = int(''.join(working_data[0]), 2)
print(ox_gen_rat)


working_data = data.copy()
for b in range(len(data[0])):
    bytes = [
        i[b]
        for i in data
    ]

    search_bit = '0' if bytes.count('0') <= bytes.count('1') else '1'

    working_data = [
        n
        for n in working_data
        if n[b] == search_bit
    ]

    if len(working_data) == 1:
        break

co_scrub_rat = int(''.join(working_data[0]), 2)
print(co_scrub_rat)

print(co_scrub_rat * ox_gen_rat)
