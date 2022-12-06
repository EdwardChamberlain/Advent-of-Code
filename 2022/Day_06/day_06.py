import sys
import os


def find_marker_index(data: str, marker_size: int) -> int:
    for i in range(len(data)):
        search_range = data[i:i+marker_size]
        if len(set(search_range)) == marker_size:
            return i+marker_size


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