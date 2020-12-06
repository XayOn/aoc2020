import sys


def move(movement, base):
    if movement in ('F', 'L'):
        return slice(base.start, base.start + (base.stop - base.start) / 2)
    return slice((base.start + (base.stop - base.start) / 2), base.stop)


def get_result(pos):
    pos_x = slice(0, 128)
    pos_y = slice(0, 8)
    for movement in [a for a in pos if a in ('F', 'B')]:
        pos_x = move(movement, pos_x)
    for movement in [a for a in pos if a in ('R', 'L')]:
        pos_y = move(movement, pos_y)
    return int(pos_x.start * 8 + pos_y.start)


results = list(get_result(a) for a in open(sys.argv[1]).readlines())
empty = set(range(1024)).difference(results)
print(max(results))
print(next(a for a in empty if a + 1 not in empty and a - 1 not in empty))
