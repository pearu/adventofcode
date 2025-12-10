import os
import numpy as np
data = '''
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day09.txt')).read()

def task1():
    points = []
    for line in data.split():
        x, y = map(int, line.split(','))
        points.append((x, y))

    max_a = 0
    for i, p0 in enumerate(points):
        for j, p1 in enumerate(points):
            a = (p0[0] - p1[0] + 1) * (p0[1] - p1[1] + 1)
            if a > max_a:
                max_a = a
    print(f'Task 1: {max_a}')

def point_in_polygon(polygon, point):
    # count rays vertical edge crossings to the right of the point
    total = 0
    for j in range(len(polygon)):
        i = j - 1 if j else len(polygon) - 1
        pi = i - 1 if i else len(polygon) - 1
        pj = 0 if j == len(polygon) - 1 else j + 1

        # first check if point is on the edge
        if (polygon[i][0] == polygon[j][0] and point[0] == polygon[i][0] and ((point[1] >= polygon[i][1] and point[1] <= polygon[j][1]) or (point[1] >= polygon[j][1] and point[1] <= polygon[i][1]))):
            return True
        elif (polygon[i][1] == polygon[j][1] and point[1] == polygon[i][1] and ((point[0] >= polygon[i][0] and point[0] <= polygon[j][0]) or (point[0] >= polygon[j][0] and point[0] <= polygon[i][0]))):
            return True
        else:
            total += ((polygon[i][0] == polygon[j][0]  # edge is vertical
                       and point[0] < polygon[i][0]    # edge is right to the point
                       and point[1] < max(polygon[i][1], polygon[j][1])  # ray crosses the edge
                       and point[1] > min(polygon[i][1], polygon[j][1]))
                      or (
                          polygon[i][1] == polygon[j][1]  # edge is horizontal
                          and point[0] < min(polygon[i][0], polygon[j][0])    # edge is right to the point
                          and point[1] == polygon[i][1]  # edge is at the same level as the point
                          and (polygon[pi][1] - point[1]) * (polygon[pj][1] - point[1]) < 0
                      )
                      )
    return total % 2 != 0

import random

def edges(p0, p1):
    lst = list(range(p0[0] + 1, p1[0]))
    random.shuffle(lst)
    for x in lst:
        yield x, p0[1]
        yield x, p1[1]
    lst = list(range(p0[1] + 1, p1[1]))
    random.shuffle(lst)
    for y in lst:
        yield p0[0], y
        yield p1[0], y

def corners(p0, p1):
    yield p0
    yield p0[0], p1[1]
    yield p1
    yield p1[0], p0[1]

def boundaries(p0, p1):
    yield from corners(p0, p1)
    yield from edges(p0, p1)

def rectangles(points):
    # NOT IMPLEMENTED IDEA: find an internal point, define the
    # internal side of the edge, yield only rectangles that internal
    # sides are not the outer sides of an edge.
    d = dict()
    recs = set()
    for p1 in points:
        for p2 in points:
            p1_ = (min(p1[0], p2[0]), min(p1[1], p2[1]))
            p2_ = (max(p1[0], p2[0]), max(p1[1], p2[1]))
            for p in points:
                # discard if a rectangle contains a point
                if p[0] > p1_[0] and p[0] < p2_[0] and p[1] > p1_[1] and p[1] < p2_[1]:
                    break
            else:
                a = (p2_[0] - p1_[0] + 1) * (p2_[1] - p1_[1] + 1)
                recs.add((a, p1_, p2_))
    # start with the largest rectangle
    for a, p1, p2 in sorted(recs, reverse=True):
        if a > 1615484160:
            continue
        print(f'{a=}')
        yield p1, p2

import functools
    
def task2():
    points = []
    for line in data.split():
        x, y = map(int, line.split(','))
        if points:
            assert x == points[-1][0] or y == points[-1][1], (x, y, points[-1])
        points.append((x, y))
    print(points)
        
    @functools.cache
    def inside(p):
        return point_in_polygon(points, p)

    for p1, p2 in rectangles(points):
        for p in boundaries(p1, p2):
            if not inside(p):
                break
        else:
            a = (p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1)
            print('Task 2:', a)
            break

if __name__ == '__main__':
    task1()
    task2()  # it takes about 25 minutes
