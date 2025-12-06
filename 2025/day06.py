import os
import numpy as np
data = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

data = open(os.path.join(os.path.dirname(__file__),'data/day06.txt')).read()
data = data.rstrip('\n')

def task1():
    lst = None
    for line in data.split('\n'):
        if lst is None:
            lst = [c == ' ' for c in line]
        else:
            assert len(lst) == len(line), (len(lst), len(line))
            lst = [f and c == ' ' for f, c in zip(lst, line)]
    lst = [0] + [i for i, f in enumerate(lst) if f] + [len(line)]

    cols = None
    for line in data.split('\n'):
        if cols is None:
            cols = [[line[i0:i1].strip()] for i0, i1 in zip(lst[:-1], lst[1:])]
        else:
            cols = [cols[k] + [line[i0:i1].strip()] for k, (i0, i1) in enumerate(zip(lst[:-1], lst[1:]))]
    c = 0
    for col in cols:
        if col[-1] == '*':
            m = 1
            for v in col[:-1]:
                m *= int(v)
            c += m
        elif col[-1] == '+':
            for v in col[:-1]:
                c += int(v)
        else:
            assert 0

    print(f'Task 1: {c}')


def task2():
    lst = None
    for line in data.split('\n'):
        if lst is None:
            lst = [c == ' ' for c in line]
        else:
            assert len(lst) == len(line), (len(lst), len(line))
            lst = [f and c == ' ' for f, c in zip(lst, line)]
    lst = [0] + [i for i, f in enumerate(lst) if f] + [len(line)]

    cols = None
    for line in data.split('\n'):
        if cols is None:
            cols = [[line[i0:i1]] for i0, i1 in zip(lst[:-1], lst[1:])]
        else:
            cols = [cols[k] + [line[i0:i1]] for k, (i0, i1) in enumerate(zip(lst[:-1], lst[1:]))]

    rcols = []
    for col in cols:
        rcol = ['' for c in range(10)]
        for i, n in enumerate((col[:-1])):
            for j, c in enumerate(n):
                rcol[j] += c
        rcols.append([n.strip() for n in rcol if n.strip()] + [col[-1].strip()])

    c = 0
    for col in rcols:
        if col[-1] == '*':
            m = 1
            for v in col[:-1]:
                m *= int(v)
            c += m
        elif col[-1] == '+':
            for v in col[:-1]:
                c += int(v)
        else:
            assert 0

    print(f'Task 2: {c}')

if __name__ == '__main__':
    task1()
    task2()
