def f(a):
    m, n = len(a), len(a[0])
    z = []
    for r in range(m):
        i = r
        j = 0
        v = []
        while j < n and i >= 0:
            v.append(a[i][j])
            i -= 1
            j += 1
        z.append(v[::-1])
    for c in range(1, n):
        i = m-1
        j = c
        v = []
        while j < n and i >= 0:
            v.append(a[i][j])
            i -= 1
            j += 1
        z.append(v[::-1])
    return z


def diagonals(m):
    if(not len(m)):return []
    if(len(m)==1 and len(m[0])==1):return [m[0]]
    one = f(m)
    two = f(list(map(lambda e: e[::-1], m)))
    one.extend(two)
    return one


print(diagonals([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]))
