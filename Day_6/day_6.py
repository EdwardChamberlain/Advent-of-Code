import question_parser


with open("Day_6/input_6.txt", 'r') as f:
    data = f.read().split('\n\n')

data = [i.split('\n') for i in data]

totals = []
for i in data:
    totals.append(question_parser.or_resp(i))

print(sum(totals))
