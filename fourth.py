import sys, re, timeit
from collections import Counter

MANDATORY = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
LMT = {'in': [59, 76], 'cm': [150, 193]}
limit = lambda x, n: LMT[x][0] <= int(n) <= LMT[x][1]
CHECKS = {
    "byr": lambda x: x.isnumeric() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: x.isnumeric() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: x.isnumeric() and 2020 <= int(x) <= 2030,
    "hgt": lambda x: LMT.get(x[-2:]) and limit(x[-2:], x[:-2]),
    "hcl": lambda x: re.match('^#[0-9a-f]{6}', x),
    "ecl": lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    "pid": lambda x: x.isnumeric() and len(x) == 9,
    "cid": lambda x: True
}
RULES = [
    lambda res: not MANDATORY.difference(res.keys()),
    lambda res: all(r(res.get(k, '')) for k, r in CHECKS.items())
]


def check_passports():
    for line in (a for a in open(sys.argv[1]).read().split('\n\n')):
        if res := dict((f.split(':') for f in line.strip().split())):
            yield all(r(res) for r in RULES[:int(sys.argv[2])])


print(Counter(check_passports())[True])
