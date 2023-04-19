import math
def f(x):
    i = 2
    r = []
    while i < math.sqrt(x)+1:
        if (x % i == 0):
            r.append(i)
            r.append(x/i)
        i += 1
    r = sorted(set(filter(lambda e: e > 1 and e != x, map(int, r))))
    return [x, r if len(r) else ['None']]


def factorsRange(n, m):
    l = list(range(n, m+1))
    return dict(list(map(f, l)))


print(factorsRange(200, 220))
