def serve(n,k,m):
    r,c,t,s=[0]*m,1,1,n+1
    if k!=1:
        for _ in range(1,m):
            c*=k
            t+=c
        s=n/t
    else:
        s=n/m
    r[0]=s
    for i in range(1,m):
        r[i]=round(r[i-1]*k,6)
    return r
        

print(serve(728,3,6))
print(serve(100,1.5,3))