import os
data = '''
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
'''.strip()

data = '''
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day11.txt')).read().strip()

from collections import defaultdict

def task1():
    d = defaultdict(list)
    for line in data.splitlines():
        node, rest = line.split(':')
        d[node] = rest[1:].split()

    def foo(start, stop):
        for next in d[start]:
            if next == stop:
                yield next
                return
            yield from foo(next, stop)

    print('Task 1', len(list(foo('you', 'out'))))

def task2():
    d = defaultdict(set)
    for line in data.splitlines():
        node, rest = line.split(':')
        d[node].update(rest[1:].split())

    def foo3(result, start, stop, tree, cache, expect):
        key = result, start
        if key in cache:
            return cache[key]
        if start in expect:
            r = result + (start,)
        else:
            r = result
        count = 0
        for next in tree[start]:
            if next == stop:
                return result == expect
            count += foo3(r, next, stop, tree, cache, expect)
        cache[key] = count
        return count

    dac_out = foo3((), 'svr', 'out', d, dict(), expect=('svr', 'fft', 'dac'))
    print(f'{dac_out=}')
    fft_out = foo3((), 'svr', 'out', d, dict(), expect=('svr', 'dac', 'fft'))
    print(f'{fft_out=}')
    print('Task 2:', dac_out + fft_out)


if __name__ == '__main__':
    task1()
    task2()
