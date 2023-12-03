import os
import sys
import re


class Numeric_Object:
    def __init__(self, start, end, row, value) -> None:
        self.start = start
        self.end = end
        self.row = row
        self.value = value


class Dataset:
    def __init__(self, array) -> None:
        self.array = array.split('\n')

        matches_by_row = [
            re.finditer(r'\d+', row)
            for row in self.array
        ]

        self.numeric_objects = [
            Numeric_Object(match.start(), match.end(), y, int(match.group()))
            for y, row in enumerate(matches_by_row)
            for match in row
        ]

    def neighbours(self, xy):
        x, y = xy
        potential = [
            (x - 1, y - 1),
            (x - 1, y + 0),
            (x - 1, y + 1),

            (x + 0, y + 1),
            (x + 0, y - 1),

            (x + 1, y - 1),
            (x + 1, y + 0),
            (x + 1, y + 1),
        ]

        result = [
            (x, y)
            for x, y in potential
            if x >= 0 and y >= 0 and x <= len(self.array[0]) - 1 and y <= len(self.array) - 1
        ]

        return result 

    def get_componennts(self):
        return [
            n
            for n in self.numeric_objects
            if self.is_component(n)
        ]

    def is_connected(self, xy):
        for x, y in self.neighbours(xy):
            if not self.array[y][x].isnumeric() and self.array[y][x] != '.':
                return True
        return False

    def is_component(self, numeric_object: Numeric_Object):
        for x in range(numeric_object.start, numeric_object.end):
            if self.is_connected((x, numeric_object.row)):
                return True
        return False

    def get_connected_gears(self, comp: Numeric_Object):
        gears = set()
        for x_posn in range(comp.start, comp.end):
            for n in self.neighbours((x_posn, comp.row)):
                x, y = n
                if self.array[y][x] == '*':
                    gears.add((x, y))

        return gears

    def collect_gear_pairs(self):
        gears = {}
        for comp in self.numeric_objects:
            connected_gears = self.get_connected_gears(comp)

            for g in connected_gears:
                if g in gears:
                    gears[g].append(comp.value)
                
                else:
                    gears[g] = [comp.value]
        
        return gears

    def gear_ratios(self):
        gears = self.collect_gear_pairs()

        ratios = []
        for connected_parts in gears.values():
            if len(connected_parts) == 2:
                ratio = connected_parts[0] * connected_parts[1]
                ratios.append(ratio)

        return ratios
        

with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
    data = f.read()

data = Dataset(data)

# Pt 1
print(
    sum(
        [
            c.value
            for c in data.get_componennts()
        ]
    )
)

# Pt 2
print(
    sum(
        data.gear_ratios()
    )
)