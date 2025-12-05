import os
import numpy as np
data = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day05.txt')).read()

def ranges_add(ranges, s0, s1):
    flag = True
    for r0, r1 in ranges.copy():
        # |---| !+++!
        if s1 < r0:
            pass
        # |--!++|++!
        elif s0 <= r0 and r0 <= s1 and s1 <= r1:
            ranges.remove((r0, r1))
            ranges.add((s0, r1))
            flag = False
        # |--!++++!--|
        elif s0 <= r0 and r1 <= s1:
            ranges.remove((r0, r1))
            ranges.add((s0, s1))
            flag = False
        # !++|++!--|
        elif r0 <= s0 and s0 <= r1 and r1 <= s1:
            ranges.remove((r0, r1))
            ranges.add((r0, s1))
            flag = False
        # !++|---|++!
        elif r0 <= s0 and s1 <= r1:
            flag = False
        # !+++! |---|
        elif r1 < s0:
            pass
        else:
            assert 0
    if flag:
        ranges.add((s0, s1))

def task1():
    ranges_data, ids_data = data.split('\n\n')
    ranges = set()
    for line in ranges_data.strip().split():
        s0, s1 = map(int, line.split('-'))
        ranges_add(ranges, s0, s1)

    c = 0
    for i in ids_data.strip().split():
        i = int(i)
        for r0, r1 in sorted(ranges):
            if r0 <= i and i <= r1:
                c += 1
                break
    print(f'Task 1: {c}')

def task2():
    ranges_data, ids_data = data.split('\n\n')
    ranges = set()
    for line in ranges_data.strip().split():
        s0, s1 = map(int, line.split('-'))
        ranges_add(ranges, s0, s1)

    def has_overlapping(ranges):
        last_r1 = None
        for r0, r1 in sorted(ranges):
            if last_r1 is not None:
                if not (last_r1 < r0):
                    return True
            last_r1 = r1
        return False

    # join overlapping ranges, actually requires only two iterations
    while has_overlapping(ranges):
        ranges2 = set()
        for s0, s1 in ranges:
            ranges_add(ranges2, s0, s1)
        ranges = ranges2

    c = 0
    for r0, r1 in ranges:
        c += r1 - r0 + 1
    print(f'Task 2: {c}')

if __name__ == '__main__':
    task1()
    task2()
