import math


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

class Ship2:
    def __init__(self, way_x=0, way_y=0):
        self.x = 0
        self.y = 0
        self.a = 0
        self.way_x = way_x
        self.way_y = way_y

    def command(self, input_code):
        input_code = self._parse_intput(input_code)

        if input_code[0] == 'R':
            self._rotate(-input_code[1])
        elif input_code[0] == 'L':
            self._rotate(input_code[1])
        elif input_code[0] == 'N':
            self.way_y += input_code[1]
        elif input_code[0] == 'E':
            self.way_x += input_code[1]
        elif input_code[0] == 'S':
            self.way_y -= input_code[1]
        elif input_code[0] == 'W':
            self.way_x -= input_code[1]
        elif input_code[0] == 'F':
            self._forward(input_code[1])

    def _forward(self, reps):
        for _ in range(reps):
            self.x += self.way_x
            self.y += self.way_y

    def _rotate(self, ang):
        ang = math.radians(ang)

        x = self.way_x
        y = self.way_y

        self.way_x = round((x * math.cos(ang)) - (y * math.sin(ang)))
        self.way_y = round((x * math.sin(ang)) + (y * math.cos(ang)))

    def _parse_intput(self, input_code):
        return (input_code[0], int(input_code[1:]))
