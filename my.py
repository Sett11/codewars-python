def expansion(m,n):
    if(not n):
        return m
    r=[]
    d=[]
    i=0
    while i<len(m):
        j=0
        while j<len(m[i]):
            if(i==j):
                d.append(m[i][j])
            j+=1
        i+=1
    i=0
    while i<len(m[0]):
        j=0
        a=[]
        while j<len(m):
            a.append(m[j][i])
            j+=1
        i+=1
        r.append(a)
    i=0
    while i<len(m):
        m[i].append(sum(m[i]))
        i+=1
    z=[]
    i=0
    while i<len(r):
        z.append(sum(r[i]))
        i+=1
    z.append(sum(d))
    m.append(z)
    return expansion(m,n-1)

print(expansion([
    [1,2],
    [5,3]
],2))