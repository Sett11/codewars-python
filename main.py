def collision(a):
    n, m, c = len(a), len(a[0]), 1
    while True:
        pos, dr, na = {}, {}, [['-'] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if a[i][j] in 'udlr':
                    t, v = (i,j), a[i][j]
                    if v == 'u':
                        pos[t] = (i-1, j)
                        dr[pos[t]] = 'u'
                    if v == 'd':
                        pos[t] = (i+1, j)
                        dr[pos[t]] = 'd'
                    if v == 'r':
                        pos[t] = (i, j+1)
                        dr[pos[t]] = 'r'
                    if v == 'l':
                        pos[t] = (i, j-1)
                        dr[pos[t]] = 'l'
        vals = pos.values()
        if len(vals) > len(set(vals)):
            return c
        if not vals:
            return -1
        for i, j in pos.items():
            if j in pos and i in vals:
                return c
            if 0 <= j[0] < n and 0 <= j[1] < m:
                na[j[0]][j[1]] = dr[j]
        c += 1
        a = na

print(collision([
                    list("-----"),
                    list("--d-l"),
                    list("-----"),
                    list("rr--u"),
                    list("--l--")
                ]),sep='\n')