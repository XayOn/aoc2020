import sys
from itertools import chain
from functools import reduce
data = open(sys.argv[1]).read().split('\n\n')
res = (set(chain(*(a for a in line.strip().split()))) for line in data)
res2 = list(list(set(a) for a in line.strip().split()) for line in data)
print(sum(len(r) for r in res))
print(sum(len(reduce(lambda x, y: x.intersection(y), ele)) for ele in res2))
