import sys
import os

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()

def find_marker(data: str, lookahead: int) -> int:
    for i in range(len(data)):
        search_range = data[i:i+lookahead]
        if len(set(search_range)) == lookahead:
            return i+lookahead

print(
    find_marker(data, 4)
)