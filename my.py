def solve(n):
    r=['0','01']
    while len(r)<=n:
        r.append(r[-1]+r[-2])
    return r[n]

print(solve(3))