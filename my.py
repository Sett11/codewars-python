def n_linear(a,n):
    r,m=[1]+[0]*n,len(a)
    k=[0]*m
    for i in range(1,n+1):
        t=[a[j]*r[k[j]]+1 for j in range(m)]
        r[i]=min(t)
        for p,j in enumerate(t):
            if j==r[i]:
                k[p]+=1
    return r[n]


print(n_linear([2,3],20))