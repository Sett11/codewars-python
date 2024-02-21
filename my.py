from math import ceil
from random import randint

def e(n=1000000):
    r=[False]*2+[True]*(n-2)
    for i in range(2,int(n**.5+1)):
        if r[i]:
            r[2*i:n:i]=[False]*ceil((n/i)-2)
    return [i for i,j in enumerate(r) if j]

a=e()

def f(n):
    i=2
    a=[1]
    for i in range(2,int(n**.5+1)):
        if n%i==0:
            a.append(i)
            a.append(n//i)
    return a+[n]

def mrt(n,k=5):
    if n<2:
        return False
    if n<4:
        return True
    r,s=0,n-1
    while s%2==0:
        r+=1
        s//=2
    for _ in range(k):
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

def mobius(n):
    for i in a:
        if i>n:
            break
        if n%i**2==0:
            return 0
    return [-1,1][len([i for i in f(n) if mrt(i)])%2==0]

print(mobius(537320679415))