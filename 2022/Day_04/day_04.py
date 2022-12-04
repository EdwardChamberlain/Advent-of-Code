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


# Pt 1
count = 0
for a, b in data:
    a = conv_int(a)
    b = conv_int(b)

    mainlist, sub_list = (b, a) if len_range(a) < len_range(b) else (a, b)

    if sub_list[0] >= mainlist[0] and sub_list[1] <= mainlist[1]:
        count += 1

print(count)


# Pt 2
count = 0
for n, d in enumerate(data):
    a = conv_int(d[0])
    b = conv_int(d[1])
    if a[0] < b[0]:
        x = a
        y = b
    else:
        x = b
        y = a

    if x[1] >= y[0]:
        count += 1

print(count)