#!/usr/bin/env python
import sys
from copy import deepcopy

grids = []
draws = []

def _sum_grid(grid):
    return sum(val for row in grid for val in row if val > 0)

def draw(grids, draws, p2 = False):
    res = 0
    won = [False] * len(grids)
    for draw in draws:
        for grid_index, grid in enumerate(grids):

            if won[grid_index]:
                continue

            for i, row in enumerate(grid):

                for j, c in enumerate(row):
                    if c == draw:
                        grid[i][j] = -1

                    col = [row[j] for row in grid]
                    if all(v == -1 for v in col):
                        won[grid_index] = True
                        if not p2:
                            return _sum_grid(grid) * draw
                        res = _sum_grid(grid) * draw

                if all(v == -1 for v in row):
                    won[grid_index] = True
                    if not p2:
                        return _sum_grid(grid) * draw
                    res = _sum_grid(grid) * draw
    return res


with open(sys.argv[1], 'r', encoding='utf-8') as file:
    draws = [int(val) for val in file.readline().strip().split(',')]

    grids = []
    grid = None
    for line in file:
        line = line.strip()
        if line == '':
            if grid:
                grids.append(grid)
            grid = []
        else:
            grid.append([int(val) for val in line.split()])

    grids.append(grid)

print('Part 1:', draw(deepcopy(grids), draws))
print('Part 2:', draw(deepcopy(grids), draws, True))
