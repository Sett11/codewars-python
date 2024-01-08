def logistic_map(m,n,x,y):
    r,z=[[None]*m for _ in range(n)],list(zip(y,x))
    if not z:
        return r
    for i,j in z:
        r[i][j]=0
    for i in range(n):
        for j in range(m):
            r[i][j]=min((abs(p-i)+abs(t-j)) for p,t in z)
    return r

print(logistic_map(5,2,[0,4],[0,0]))

[[0, 1, 2, 1, 0],
 [1, 2, 1, 0, 1]]