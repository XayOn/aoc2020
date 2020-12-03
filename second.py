"""Day 2"""
import re, sys
from collections import Counter

LNS = re.compile('(\d+)-(\d+) (\w): (.*)')
IN = lambda x: int(x) - 1
POLS = [
    lambda m, x, l, s: int(m) <= Counter(s)[l] <= int(x),
    lambda m, x, l, s: Counter(a == l for a in (s[IN(m)], s[IN(x)]))[True] == 1
]
res = open(sys.argv[1]).readlines()
print(len([l for l in res if POLS[int(sys.argv[2])](*LNS.match(l).groups())]))
