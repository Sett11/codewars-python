def highest_prod(a):
    m = 0
    def k(a):
        nonlocal m
        t = r = 1
        for i in a:
            m = max(m, i)
            t *= i
            if t > r:
                r = t
            if t < 1:
                t = 1
        return r
    r = max(list(map(k, a)) + list(map(k, zip(*a))))
    return r if r != m else 0

print(highest_prod([[2, 1, 4, 1], [0, 4, 8, 1], [1, 0, 10, 0]]))
print(highest_prod([[2, 0, 4, 0], [0, 0, 0, 0], [1, 0, 10, 0]]))