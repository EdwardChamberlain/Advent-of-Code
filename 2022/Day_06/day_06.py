import sys
import os


def find_marker(data: str, lookahead: int) -> int:
    for i in range(len(data)):
        search_range = data[i:i+lookahead]
        if len(set(search_range)) == lookahead:
            return i+lookahead


with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()

# Pt 1
print(
    find_marker(data, 4)
)

# Pt 2
print(
    find_marker(data, 14)
)