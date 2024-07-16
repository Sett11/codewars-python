def fit_in(a,b,m,n):
    try:
        t,q=sorted([m,n]),sorted([a,b])
        r=[[0]*t[1] for _ in range(t[0])]
        for i in range(q[1]):
            for j in range(q[1]):
                r[i][j]=1
        r=[[j for j in i if not j] for i in r]
        return len(r)>=q[0] and len(r[0])>=q[0]
    except IndexError:
        return 1==2

print(fit_in(7,1,7,8))