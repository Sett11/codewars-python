def S2N(m,n,c=0,i=0):
    l=list(range(0,m+1))
    while i<=n:
        c+=sum(map(lambda e: e**i,l))
        i+=1
    return c

print(S2N(10,9))