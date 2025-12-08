import os
import numpy as np
data = '''
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''.strip()

data = open(os.path.join(os.path.dirname(__file__),'data/day08.txt')).read()

def task1():
    junctions = dict()
    distance = dict()
    for k, line in enumerate(data.split()):
        p0 = tuple(map(int, line.split(',')))
        for k_ in junctions:
            p = junctions[k_]
            distance[k, k_] = sum([(x0 - x)**2 for x0, x in zip(p0, p)])
        junctions[k] = p0

    if len(junctions) == 1000:
        N = 1000
    else:
        N = 10
        
    circuits = []
    for i, (_, (k0, k)) in enumerate(sorted([(d, (k0, k)) for (k0, k), d in distance.items()])):
        c0 = ([c for c in circuits if k0 in c] or [None])[0]
        c = ([c for c in circuits if k in c] or [None])[0]
        if c0 is None:
            if c is None:
                circuits.append({k0, k})
            else:
                c.add(k0)
        elif c is None:
            c0.add(k)
        else:
            c1 = set()
            c1.update(c0)
            c1.update(c)
            circuits.append(c1)
            c0.clear()
            c.clear()
            circuits = [c for c in circuits if c]

        if i == N - 1:
            break

    import math
    print('Task 1:', math.prod(sorted(map(len, circuits), reverse=True)[:3]))

def task2():
    junctions = dict()
    distance = dict()
    for k, line in enumerate(data.split()):
        p0 = tuple(map(int, line.split(',')))
        for k_ in junctions:
            p = junctions[k_]
            distance[k, k_] = sum([(x0 - x)**2 for x0, x in zip(p0, p)])
        junctions[k] = p0

    circuits = []
    for _, (k0, k) in sorted([(d, (k0, k)) for (k0, k), d in distance.items()]):
        c0 = ([c for c in circuits if k0 in c] or [None])[0]
        c = ([c for c in circuits if k in c] or [None])[0]
        if c0 is None:
            if c is None:
                circuits.append({k0, k})
            else:
                c.add(k0)
        elif c is None:
            c0.add(k)
        else:
            c1 = set()
            c1.update(c0)
            c1.update(c)
            circuits.append(c1)
            c0.clear()
            c.clear()
            circuits = [c for c in circuits if c]

        if len(circuits) == 1 and len(circuits[0]) == len(junctions):
            print('Task 2:', junctions[k][0] * junctions[k0][0])
            break


if __name__ == '__main__':
    task1()
    task2()
