import collections
import connections


with open("Day_10/input_10.txt", 'r') as f:
    data = f.readlines()
data = [int(i) for i in data]

device_jolts = max(data) + 3

all_transformers = data
all_transformers.append(0)
all_transformers.append(device_jolts)

steps = []
for i, j in enumerate(sorted(all_transformers)):
    if j == 0:
        continue
    steps.append(connections.calc_delta(j, sorted(all_transformers)[i-1]))

result = collections.Counter(steps)
print('Result for pt 1:', result[1] * result[3])

forward_connections = connections.all_forward_connections(all_transformers)
print('Result for pt 2:', connections.calcualte_possible_permutations(0, forward_connections, max(data)))
