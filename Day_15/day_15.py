data = [13,16,0,12,15,1]
data2 = data.copy()

LEN = 2020
LEN2 = 30000000

def rindex(search, data):
    return len(data) - list(reversed(data)).index(search) 

def append_number(data):
    try:
        next_num = len(data) - rindex(data[-1], data[:-1])
    except ValueError:
        next_num = 0
    data.append(next_num)
    return data

def get_next_number(current, index, hist):
    try:
        return (index + 1) - (hist[current] + 1)
    except KeyError:
        return 0


for i in range(LEN - len(data)):
    data = append_number(data)

print(f"Pt 1: {data[-1]}")

# ~~~~~~~~~~ Pt 2 ~~~~~~~~~~

input_list = data2

current = input_list[-1]
history = {v:i for i, v in enumerate(input_list[:-1])}

for i in range(len(input_list)-1, LEN2-1):
    result = get_next_number(current, i, history)
    history[current] = i
    current = result

    if i % 50000 == 0:
        print(f"Solving Pt2: |{'█'*int(i/30000000*20):░<20}|{i/30000000*100:>3.0f}%|{i:>10,}|", end='\r')

print(f"Pt 2: {result}{' '* 50}")
