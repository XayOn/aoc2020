"""Day 1

First part: python3.8 first.py input_file 2 # Match two elements
Second part: python3.8 first.py input_file 3 # Match three elements
"""

import sys
from itertools import product, accumulate
from operator import add, mul

if __name__ == "__main__":
    nums = open(sys.argv[1]).readlines()
    res = next(
        list(accumulate(a, mul))[-1]
        for a in product(*[[int(a) for a in nums]] * int(sys.argv[2]))
        if list(accumulate(a, add))[-1] == 2020)
    print(res)
