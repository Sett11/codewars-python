def SJF(a,b):
    s,i=0,-1
    while i!=b:
        m=min(a)
        n=a.index(m)
        s+=m
        a[n]=float('inf')
        i=n
    return s

print(SJF([3, 10, 20, 1, 2, 10, 10],5))