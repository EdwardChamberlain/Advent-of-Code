# Open Data
with open("Day_1/input_1.txt", 'r') as f:
    data = f.readlines()

# Convert to int
data = [int(i.strip()) for i in data]

# Loop over looking for sum = 2020
for v in data:
    for t in data:
        if v + t == 2020:
            print(f"{v} + {t} = 2020!\n{v} x {t} = {v * t}")
            exit()