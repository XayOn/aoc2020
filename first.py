"""Day 1"""
import sys
from itertools import product
from functools import reduce
from operator import add, mul

nms = [[int(a) for a in open(sys.argv[1]).readlines()]] * int(sys.argv[2])
print(next(reduce(mul, a) for a in product(*nms) if reduce(add, a) == 2020))
