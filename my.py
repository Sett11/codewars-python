from random import randint
from bisect import insort

def mrt(n,k=5):
    if n<2:
        return False
    if n<4:
        return True
    r,s=0,n-1
    while s%2==0:
        r+=1
        s//=2
    for __ in range(k):
        a=randint(2,n-1)
        x=pow(a,s,n)
        if x in [1,n-1]:
            continue
        for __ in range(r):
            x=pow(x,2,n)
            if x==n-1:
                break
        else:
            return False
    return True

def f(n):
    a=[1,n]
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            a.extend([i,n//i])
    return len(set(a))

def proc_arrInt(a):
    p,d,m=len(list(filter(mrt,a))),{},0
    for i in a:
        t=f(i)
        m=max(t,m)
        if t not in d:
            d[t]=[i]
        else:
            insort(d[t],i)
    return [len(a),p,[m,d[m]]]

print(proc_arrInt([267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445,
        67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379]))