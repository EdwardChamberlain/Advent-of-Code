import sys
import os

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()
    data = data.split('\n')
