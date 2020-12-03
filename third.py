"""Third day"""
from operator import mul
from functools import reduce
from collections import Counter
import sys


def traverse_grid(grid, step_x, step_y, curr_pos=0):
    for pos_x in range(step_x, len(grid), step_x):
        curr_pos += step_y
        yield grid[pos_x][curr_pos % len(grid[pos_x])] == '#'


grid = [[a for a in a if a != '\n'] for a in open(sys.argv[1]).readlines()]
slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
res = [Counter(traverse_grid(grid, *slope))[True] for slope in slopes]
print(dict(zip(slopes, res)))
print(reduce(mul, res))
