import os
import numpy as np
data = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day04.txt')).read()

def task1():
    c = 0
    lines = []
    for line in data.split():
        lines.append([0] + [{'.': 0, '@': 1}[c] for c in line] + [0])
    lines.insert(0, [0] * len(lines[0]))
    lines.append([0] * len(lines[0]))

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            s = 0
            for m in [-1, 0, 1]:
                for n in [-1, 0, 1]:
                    if m == 0 and n == 0:
                        continue
                    s += lines[i + m][j + n]
            if lines[i][j] and s < 4:
                c += 1

    print(f'Task 1: {c}')

def task2():
    roles = set()
    for i, line in enumerate(data.split()):
        for j, c in enumerate(line):
            if c == '@':
                roles.add((i, j))
    flag = True
    c = 0
    while flag:
        flag = False
        for i, j in roles.copy():
            s = 0
            for m, n in [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)
            ]:
                s += (i + m, j + n) in roles
                if s >= 4:
                    break
            else:
                roles.remove((i, j))
                flag = True
                c += 1            
    print(f'Task 2: {c}')

if __name__ == '__main__':
    task1()
    task2()
