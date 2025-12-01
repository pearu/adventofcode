import os
data = '''
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
'''

data = open(os.path.join(os.path.dirname(__file__),'data/day01.txt')).read()

def task1():
    p = 50
    c = 0
    for line in data.strip().split():
        d = dict(L=-1, R=1)[line[0]]
        s = int(line[1:])
        p = (p + d * s) % 100
        if p == 0:
            c += 1
    print(f'Task 1: {c=}')

def task2():
    p = 50
    c = 0
    for line in data.strip().split():
        d = dict(L=-1, R=1)[line[0]]
        s = int(line[1:])
        for s_ in range(s):
            p += d
            p = p % 100
            if p == 0:
                c += 1
    print(f'Task 2: {c=}')

if __name__ == '__main__':
    task1()
    task2()
