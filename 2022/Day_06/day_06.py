import sys
import os

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()

for i in range(len(data)):
    buff = data[i:i+4]
    print(buff, set(buff), len(set(buff)))
    if len(set(buff)) == 4:
        print("Marker at ", i+4)
        break