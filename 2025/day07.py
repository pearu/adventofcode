import os
import numpy as np
data = '''
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day07.txt')).read()

def task1():
    c = 0
    beams = set()
    for i, line in enumerate(data.split()):
        if i == 0:
            beams.add(line.index('S'))
            continue
        splitters = [j for j, c in enumerate(line) if c == '^']
        if not splitters:
            continue

        for b in beams.copy():
            for s in splitters:
                if b == s:
                    beams.add(s - 1)
                    beams.add(s + 1)
                    beams.remove(s)
                    c += 1
    print(f'Task 1: {c}')


def task2():
    from collections import defaultdict
    beams = defaultdict(int)
    for i, line in enumerate(data.split()):
        if i == 0:
            beams[line.index('S')] += 1
        else:
            for j, c in enumerate(line):
                if c == '^':
                    beams[j+1] += beams[j]
                    beams[j-1] += beams[j]
                    del beams[j]
    c = sum(beams.values())
    print(f'Task 2: {c}')

if __name__ == '__main__':
    task1()
    task2()
