import os
data = '''
987654321111111
811111111111119
234234234234278
818181911112111
'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day03.txt')).read()

def task1():
    c = 0
    for line in data.split():
        j0 = 0
        j1 = 0
        for n, j in enumerate(line):
            j = int(j)
            if j > j0 and n < len(line) - 1:
                j0 = j
                j1 = 0
            elif j > j1:
                j1 = j
        c += 10 * j0 + j1
    print(f'Task 1: {c=}')

def task2():
    N, c = 12, 0
    for line in data.split():
        r = ''
        for i in range(N - 1):
            r += max(line[:-N + 1 + i])
            line = line[line.index(r[-1]) + 1:]
        c += int(r + max(line))
    print(f'Task 2: {c=}')

if __name__ == '__main__':
    task1()
    task2()
