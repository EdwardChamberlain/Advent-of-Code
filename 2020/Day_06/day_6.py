import question_parser


with open("Day_6/input_6.txt", 'r') as f:
    data = f.read().split('\n\n')
data = [i.split('\n') for i in data]

totals = []
for i in data:
    totals.append(question_parser.or_resp(i))

print(f"Total pt1: {sum(totals)}")

totals = []
for i in data:
    totals.append(question_parser.count_response2(i))

print(f"Total pt2: {sum(totals)}")