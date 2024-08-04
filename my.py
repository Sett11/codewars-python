def dbl_linear(n):
    r=[1]+[0]*n
    k=j=0
    for i in range(1,n+1):
        x,y=2*r[k]+1,3*r[j]+1
        r[i]=min(x,y)
        if r[i]==x:
            k+=1
        if r[i]==y:
            j+=1
    return r[n]


print(dbl_linear(50))