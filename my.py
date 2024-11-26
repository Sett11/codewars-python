def rule30(a,n):
    r={(0,0,0):0,(0,0,1):1,(0,1,0):1,(0,1,1):1,(1,0,0):1,(1,0,1):0,(1,1,0):0,(1,1,1):0}
    while n:
        a=[0]+a+[0]
        q=a[:]
        for i in range(len(a)):
            q[i]=r[tuple([a[i-1] if i else 0,a[i],a[i+1] if i!=len(a)-1 else 0])]
        a=q
        n-=1
    return a

print(rule30([1],5))