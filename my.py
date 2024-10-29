from gmpy2 import is_prime
from functools import reduce
from operator import mul
from itertools import permutations
from collections import Counter,defaultdict

def pf(n):
    r,c=[],2
    while c<n*n:
        while n%c==0:
            r.append(c)
            n//=c
        c+=1
    return r[::-1]

def f(a,j,r,q):
    if not r:
        t=[]
        for i in range(j):
            t.append(a[i])
        q.append(t)
        return
    for i in range(1 if not j else a[j-1],r+1):
        a[j]=i
        f(a,j+1,r-i,q)
    return q

def gen_res(a,b):
    # r,m1,m2=defaultdict(list),0,float('inf')
    r=[]
    for i in b:
        t,q=a.copy(),[]
        for j in i:
            w,k=[],j
            while k:
                w.append(t.pop())
                k-=1
            q.append([x**y for x,y in Counter(w).items()])
        r.append(sorted([reduce(mul,z) for z in q],reverse=True))
    return r

def find_spec_prod_part(n,c):
    if is_prime(n):
        return 'It is a prime number'
    a=pf(n)
    l,m1,m2,d=len(a),0,float('inf'),defaultdict(list)
    s=sum(map(list,map(set,map(permutations,f([0]*l,0,l,[])[:-1]))),[])
    r=gen_res(a,s)+gen_res(a[:1]+a[1:][::-1],s)+gen_res(a[:2]+a[2:][::-1],s)
    for i in r:
        t=reduce(lambda x,y:x+y[0]**y[1],Counter(i).items(),0)*len(i)
        m1,m2=max(m1,t),min(m2,t)
        d[t].append(i)
    return [d[m1][0],m1] if c=='max' else [d[m2][0],m2]
    

print(find_spec_prod_part(6859,'max'))
print(find_spec_prod_part(7881,'max'))
print(find_spec_prod_part(2116,'max'))