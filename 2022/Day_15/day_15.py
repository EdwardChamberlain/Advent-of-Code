import sys
import os
import numpy as np
import re
import cProfile
import itertools


def manhatten_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def load_data():
    with open(os.path.dirname(sys.argv[0]) + "/input.txt", 'r') as f:
        data = f.read()
    return data


def parse_data(data):
    data = data.split('\n')
    data = [
        re.search(r'(?:Sensor at (?:x=(.*), y=(.*)): closest beacon is at (?:x=(.*), y=(.*)))', d).groups()
        for d in data
    ]
    data = [list(map(int, d)) for d in data]
    data = [((d[0], d[1]), (d[2], d[3])) for d in data]
    return data


def a_in_b(a, b):
    return len([i for i in a if i in b])


def flaten_list(data):
    data = list(zip(*data))
    data = data[0] + data[1]
    return data


def find_intersection_points(sensor, radius, line_height):
    x, y = sensor
    horizontal = radius - abs(y - line_height)
    result = (x - horizontal, x + horizontal)
    return result


def find_objects_on_row(data, target_row):
    return set([i[0] for i in flaten_list(data) if i[1] == target_row])    
    

def get_consumed_spaces(intersections):
    consumed_spaces = []
    for i in intersections:
        consumed_spaces.extend(list(range(i[0], i[1]+1)))
    return consumed_spaces


def calcualte_solution(consumed_spaces, data, target_row):
    unique_points = set(consumed_spaces)
    objects_on_row = find_objects_on_row(data, target_row)
    overlaps = a_in_b(unique_points, objects_on_row)
    return len(unique_points) - overlaps


def pt_1(data):
    target_row = 2000000

    intersections = []
    for d in data:
        sensor, beacon = d
        radius = manhatten_distance(sensor, beacon)

        y_pos = sensor[1]

        if (y_pos >= target_row and y_pos - radius <= target_row) or (y_pos <= target_row and y_pos + radius >= target_row):
            intersection = find_intersection_points(sensor, radius, target_row)
            intersections.append(intersection)

    consumed_spaces = get_consumed_spaces(intersections)
    solution = calcualte_solution(consumed_spaces, data, target_row)
    print(solution)


def merge_intersections(intersections):
    intersections = sorted(intersections)
    ranges = []
    for i in intersections:
        if ranges == []:
            ranges = [i[0], i[1]]

        else:
            if ranges[1] + 1 < i[0]:
                break
            else:
                if i[1] > ranges[1]:
                    ranges[1] = i[1]

    return ranges


def line_scanner(data, target_row=2000000):
    intersections = []
    for d in data:
        sensor, beacon = d
        radius = manhatten_distance(sensor, beacon)

        y_pos = sensor[1]

        if (y_pos >= target_row and y_pos - radius <= target_row) or (y_pos <= target_row and y_pos + radius >= target_row):
            intersection = find_intersection_points(sensor, radius, target_row)
            intersections.append(intersection)

    ranges = merge_intersections(intersections)
    if ranges[0] <= 0 and ranges[1] >= 4000000:
        return False
    else:
        return ranges[1]


def pt_2(data):
    for i in range(4000000):
        if x := line_scanner(data, i):
            print(i, x+1)
            print((x+1) * 4000000 + i)
            break
    

if __name__ == '__main__':
    data = load_data()
    data = parse_data(data)

    pt_1()
    pt_2()