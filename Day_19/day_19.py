import message_parser


with open("Day_19/input_19.txt", 'r') as f:
    data = [i.split('\n') for i in f.read().split('\n\n')]

rules = {}
for i in data[0]:
    split = i.split(': ')
    rules[int(split[0])] = split[1]

regex = message_parser.rec_resolve_rule(rules[0], rules)
result = [message_parser.is_complient(i, regex) for i in data[1]]
print(f"Pt 1: {sum(result)}")