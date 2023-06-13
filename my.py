def expand(m,f):
    n,a=len(m)*2,[]
    while len(a)<n:
        a.append(f)
    while len(m)<n:
        m.append(a)
        m.insert(0,a)
    for i in m:
        while len(i)<n:
            i.append(f)
            i.insert(0,f)
    return m

print(expand([[1, 1],[1, 1]],0))