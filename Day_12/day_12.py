import math


with open("Day_12/input_12.txt", 'r') as f:
    data = [i.strip() for i in f.readlines()]

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.a = 0

    def command(self, input_code):
        input_code = self._parse_intput(input_code)

        if input_code[0] == 'R':
            self.a -= input_code[1]
        elif input_code[0] == 'L':
            self.a += input_code[1]
        elif input_code[0] == 'N':
            self.y += input_code[1]
        elif input_code[0] == 'E':
            self.x += input_code[1]
        elif input_code[0] == 'S':
            self.y -= input_code[1]
        elif input_code[0] == 'W':
            self.x -= input_code[1]
        elif input_code[0] == 'F':
            self._forward(input_code[1])

    def _forward(self, dist):
        angle = self.a - 360 * math.floor(self.a/360)

        if angle == 0:
            self.x += dist
        elif angle == 180:
            self.x -= dist
        elif angle == 90:
            self.y += dist
        elif angle == 270:
            self.y -= dist 

    def _parse_intput(self, input_code):
        return (input_code[0], int(input_code[1:]))

myShip = Ship()

for d in data:
    myShip.command(d.strip())

mh_dist = abs(myShip.x) + abs(myShip.y)

print(f"Pt 1 Solution: {mh_dist}")