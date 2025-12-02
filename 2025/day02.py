import os
data = "".join('''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
'''.split())

data = open(os.path.join(os.path.dirname(__file__),'data/day02.txt')).read()

def task1():
    c = 0
    for r in data.split(','):
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            s = str(i)
            if s[:len(s) // 2] == s[len(s)//2:]:
                c += i
    print(f'Task 1: {c}')

def task2():
    c = 0
    for r in data.split(','):
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            s = str(i)
            for n in range(1, len(s) // 2 + 1):
                if len(s) % n == 0:
                    p = s[:n]
                    if p * (len(s) // n) == s:
                        c += i
                        break
    print(f'Task 2: {c}')

if __name__ == '__main__':
    task1()
    task2()
