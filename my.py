def path_counter(a):
    n,m=len(a),len(a[0])
    r,d,u=[[0]*m for _ in range(n)],{},set()

    def f(i,j,q):
        while True:
            t=i,j
            if a[i][j]=='f':
                d[t]=0
            if t in d:
                for x,y in enumerate(q[::-1]):
                    d[y]=d[t]+x+1
                return
            if t in u or t in q:
                u.update(q)
                return
            q.append(t)
            if a[i][j]=='r':
                i,j=i,(j+1)%m
            elif a[i][j]=='l':
                i,j=i,j-1 if j-1>=0 else m-1
            elif a[i][j]=='u':
                i,j=i-1 if i-1>=0 else n-1,j
            elif a[i][j]=='d':
                i,j=(i+1)%n,j

    for i in range(n):
        for j in range(m):
            t=i,j
            if t in u:
                r[i][j]=-1
            else:
                if t not in d:
                    f(i,j,[])
                r[i][j]=d.get(t,-1)
    return r

print(path_counter(
"""rrrrrrrd
rrrrrrrd
rrrrrrrd
rrrrrrrd
rrrrrrrf
""".splitlines()))