import message_parser


with open("2020/Day_19/input_19.txt", 'r') as f:
    data = [i.split('\n') for i in f.read().split('\n\n')]

rules = {}
for i in data[0]:
    split = i.split(': ')
    rules[int(split[0])] = split[1]

regex = message_parser.rec_resolve_rule(rules[0], rules, specials=False)
result = [message_parser.is_complient(i, regex) for i in data[1]]
print(f"Pt 1: {sum(result)}")


# ~~~~~~~~~~ Pt 2 ~~~~~~~~~~

rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

regex = message_parser.rec_resolve_rule(rules[0], rules, specials=True)
result = [i for i in data[1] if message_parser.is_complient(i, regex)]
print(f"Pt 2: {len(result)}")
