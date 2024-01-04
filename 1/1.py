#!/usr/bin/env python
import sys

arr = []
with open(sys.argv[1], 'r', encoding='utf-8') as file:
    for line in file:
        arr.append(int(line.strip()))

p1_res = 0
for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        p1_res += 1
print("Part1:", p1_res)

p2_res = 0
for i in range(0, len(arr) - 3):
    s_1 = arr[i] + arr[i + 1] + arr[i + 2]
    s_2 = arr[i + 1] + arr[i + 2] + arr[i + 3]
    if s_2 > s_1:
        p2_res += 1
print("Part2:", p2_res)
