#!/usr/bin/env python
import sys
import math
from copy import deepcopy

report = []
with open(sys.argv[1], 'r', encoding='utf-8') as file:
    for line in file:
        report.append([int(val) for val in line.strip()])

R, C = len(report), len(report[0])
cols = []

for r in report:
    for index, c in enumerate(r):
        if index < len(cols):
            cols[index] += c
        else:
            cols.append(c)

gamma, epsilon = '', ''

for c in cols:
    if c > R // 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print('Part 1:', int(gamma, 2) * int(epsilon, 2))

oxigen_filter, co2_filter = deepcopy(report), deepcopy(report)

nb_row = R
oxygen_cols = deepcopy(cols)
for index, c in enumerate(oxygen_cols):
    if len(oxigen_filter) == 1:
        break
    filt = 1 if c >= math.ceil((nb_row) / 2) else 0

    for line in report:
        if line[index] != filt and line in oxigen_filter:
            oxigen_filter.remove(line)
            nb_row -= 1
            for idx, v in enumerate(line):
                if v == 1:
                    oxygen_cols[idx] -= 1


oxygen_rating = int(''.join(str(val) for val in oxigen_filter[0]), 2)

nb_row = R
co2_cols = deepcopy(cols)
for index, c in enumerate(co2_cols):
    if len(co2_filter) == 1:
        break
    filt = 0 if c >= math.ceil(nb_row / 2) else 1

    for line in report:
        if line[index] != filt and line in co2_filter:
            co2_filter.remove(line)
            nb_row -= 1
            for idx, v in enumerate(line):
                if v == 1:
                    co2_cols[idx] -= 1

co2_rating = int(''.join(str(val) for val in co2_filter[0]), 2)

print('Part 2:', oxygen_rating * co2_rating)
