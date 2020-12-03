"""Day 1

First part: python3.8 first.py input_file 2 # Match two elements
Second part: python3.8 first.py input_file 3 # Match three elements
"""

import sys
from itertools import product
from functools import reduce
from operator import add, mul

nms = [[int(a) for a in open(sys.argv[1]).readlines()]] * int(sys.argv[2])
print(next(reduce(mul, a) for a in product(*nms) if reduce(add, a) == 2020))
