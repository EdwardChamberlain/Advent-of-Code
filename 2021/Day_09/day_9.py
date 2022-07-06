with open('2021/Day_09/input.txt') as f:
    data = f.read()
    data = data.split('\n')



for line in data:
    chunks = {
        '()': 0,
        '[]': 0,
        '<>': 0,
        '{}': 0,
    }

    for i in line:
        if i == '(':
            chunks['()'] += 1
        if i == ')':
            chunks['()'] -= 1

        if i == '[':
            chunks['[]'] += 1
        if i == ']':
            chunks['[]'] -= 1

        if i == '<':
            chunks['<>'] += 1
        if i == '>':
            chunks['<>'] -= 1

        if i == '{':
            chunks['{}'] += 1
        if i == '}':
            chunks['{}'] -= 1

    for k, v in chunks.items():
        print(f"{k}: {v}")

    if any(chunks.values()):
        print(True)

{([(<{}[<>[]}>{[]{[(<()>