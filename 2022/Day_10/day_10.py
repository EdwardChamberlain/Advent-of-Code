import sys
import os


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n') 

x = 1
hist = [x]
for cmd in data:
    if cmd == 'noop':
        hist.append(x)
        continue

    if cmd.startswith('addx'):
        hist.append(x)
        cmd = cmd.split(' ')
        x += int(cmd[1])
        hist.append(x)


# Pt 1
strengths = [
    hist[n-1] * n
    for n in range(20, 221, 40)
]
print(sum(strengths))


# Pt 2
get_col = lambda x: x % 40
is_masked = lambda mask, pos: pos in (mask - 1, mask, mask + 1)

disp = []
for i in range(len(hist)):
    if is_masked(hist[i], get_col(i)):
        disp.append('█')
    else:
        disp.append(' ')

for i, d in enumerate(disp[:240]):
    print(d, end='')
    if ((i+1) % 40) == 0:
        print()
