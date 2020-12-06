"""Fourth. Shamelessly copied a better idea from AlejandroSCF
https://github.com/alejandroscf/advent-20/blob/main/05/1.py
"""
import sys, functools

M = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
results = frozenset(
    int(functools.reduce(lambda x, y: f'{M.get(x, x)}{M.get(y, y)}', r), 2)
    for r in open(sys.argv[1]).readlines())
empty = frozenset(range(1024)).difference(results)
print(max(results))
print(next(a for a in empty if a + 1 in results and a - 1 not in empty))
