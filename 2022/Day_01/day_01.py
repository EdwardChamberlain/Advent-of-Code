import sys
import os

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.readlines()
    data = [d.strip() for d in data]

