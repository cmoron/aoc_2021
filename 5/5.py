#!/usr/bin/env python
import sys
from collections import defaultdict

vents = []
with open(sys.argv[1], 'r', encoding='utf-8') as file:
    for line in file:

        x1, y1, x2, y2 = [int(val) for val in line.strip().replace(' -> ', ',').split(',')]

        x1x2, y1y2 = sorted([x1, x2]), sorted([y1, y2])
        vents.append([x1, y1, x2, y2])

env = defaultdict(int)

p1_res = 0
p2_res = 0
for vent in vents:
    x1, y1, x2, y2 = vent

    # p1
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            env[(x, y1)] += 1
            if env[(x, y1)] == 2:
                p1_res += 1
                p2_res += 1
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            env[(x1, y)] += 1
            if env[(x1, y)] == 2:
                p1_res += 1
                p2_res += 1

# p2
for vent in vents:
    x1, y1, x2, y2 = vent

    if x1 != x2 and y1 != y2:
        xstep = 1 if x2 > x1 else -1
        ystep = 1 if y2 > y1 else -1
        x, y = x1, y1
        while x != x2 + xstep and y != y2 + ystep:
            env[(x, y)] += 1
            if env[(x, y)] == 2:
                p2_res += 1
            x += xstep
            y += ystep

print('Part1:', p1_res)
print('Part2:', p2_res)
