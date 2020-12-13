import ship


with open("Day_12/input_12.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

myShip = ship.Ship()

for d in data:
    myShip.command(d.strip())

mh_dist = abs(myShip.x) + abs(myShip.y)

print(f"Pt 1 Solution: {mh_dist}")

# ~~~~~~~~~~ Pt 2 ~~~~~~~~~~

myShip = ship.Ship2(10, 1)

for i, d in enumerate(data):
    myShip.command(d.strip())

mh_dist = abs(myShip.x) + abs(myShip.y)

print(f"Pt 2 Solution: {mh_dist}")