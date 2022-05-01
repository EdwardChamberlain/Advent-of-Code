import binary_parser
import re
            

with open("2020/Day_14/input_14.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

# ~~~~~~~~~~ Pt 1 ~~~~~~~~~~

result = {}
for i in data:
    if i.startswith('mask'):
        mask = i.split(' ')[2]
    else:
        regex = re.search(r'mem\[(\d+)\] = (\d+)', i)
        masked_cmd = binary_parser.mask_value(regex[2], mask)
        result[regex[1]] = masked_cmd

print(f"Pt 1: {sum(result.values())}")

# ~~~~~~~~~~ Pt 2 ~~~~~~~~~~

result = {}
for i in data:
    if i.startswith('mask'):
        mask = i.split(' ')[2]
    else:
        regex = re.search(r'mem\[(\d+)\] = (\d+)', i)
        masked_add = binary_parser.apply_masking(regex[1], mask)
        all_addresses = binary_parser.get_all_addresses(masked_add)
        
        for i in all_addresses:
            result[i] = int(regex[2])

print(f"Pt 2: {sum(result.values())}")
