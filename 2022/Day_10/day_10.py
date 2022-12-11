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
def get_col(x: int) -> int:
    return x % 40


def is_masked(mask_position: int, position: int) -> bool:
    mask_positions = (mask_position - 1, mask_position, mask_position + 1)
    return position in mask_positions


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
