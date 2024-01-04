#!/usr/bin/env python
import sys

p1_d, p1_h = 0, 0
p2_d, p2_h, a = 0, 0, 0
dc = {"up": -1, "down": 1}

with open(sys.argv[1], 'r', encoding='utf-8') as file:
    for line in file:
        command, units  = line.strip().split()

        if command in dc:
            p1_d += dc[command] * int(units)
            a += dc[command] * int(units)
        else:
            p1_h += int(units)
            p2_h += int(units)
            p2_d += int(units) * a

print("Part1:", p1_d * p1_h)
print("Part2:", p2_d * p2_h)
