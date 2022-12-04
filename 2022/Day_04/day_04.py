import sys
import os


def conv_int(x):
    x = x.split('-')
    x = list(map(int, x))
    return x


def len_range(x):
    return x[1] - x[0]


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 
    data = [d.split(',') for d in data]
    data = [(conv_int(d[0]), conv_int(d[1])) for d in data]


count_a = 0
count_b = 0
for a, b in data:
    mainlist, sub_list = (b, a) if len_range(a) < len_range(b) else (a, b)


    # Pt 1 
    if sub_list[0] >= mainlist[0] and sub_list[1] <= mainlist[1]:
        count_a += 1
    
    # Pt 2
    if mainlist[1] >= sub_list[0]:
        count_b += 1

    
print(count_a)
print(count_b)