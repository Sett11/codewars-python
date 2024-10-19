import gmpy2 as g
from string import digits as d,ascii_uppercase as s
from bisect import bisect_right as b
from functools import cache

@cache
def f(n,b):
    a,r=(d+s+s.lower())[:b],''
    while n:
        r=a[n%b]+r
        n//=b
    return r

def e(n):
    l=g.isqrt(n)-1
    n-=1
    b=g.xmpz(3)
    b[4:n:2]=-1
    for i in b.iter_clear(2,l):
        b[i*i:n:i+i]=-1
    return list(b.iter_clear(2,n))

p=e(10000)

def prime_reflections(n,m):
    a,d=p[:b(p,n)],{}
    for i in range(2,m+1):
        t,u,d[i]=set(f(j,i) for j in a),set(),0
        for j in t:
            k=j[::-1]
            if k in t and j not in u and k not in u and j!=j[::-1]:
                d[i]+=1
                u.add(j)
    return d

print(prime_reflections(27,18))