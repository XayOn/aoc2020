"""Day 2

First part: python3.8 first.py input_file 0 # First policy
Second part: python3.8 first.py input_file 1 # Second policy
"""

import re
import sys
from collections import Counter

PARSE_LINE = re.compile('(\d+)-(\d+) (\w): (.*)')
POLICIES = [
    lambda m, x, l, s: m <= Counter(s)[l] <= x,
    lambda m, x, l, s: Counter(a == l for a in (s[m - 1], s[x - 1]))[True] == 1
]


def get_valid_passwords(policy, entries):
    for line in entries:
        min_, max_, letter, string = PARSE_LINE.match(line).groups()
        yield policy(int(min_), int(max_), letter, string)


lines = open(sys.argv[1]).readlines()
print(Counter(get_valid_passwords(POLICIES[int(sys.argv[2])], lines))[True])
