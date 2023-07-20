import math
from functools import reduce

def convert(n,b):
    a,r='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[:b],''
    while n>0:
        r=a[n%b]+r
        n//=b
    return r

def primes_checker(n):
    if n<2:
        return False
    if n==2:
        return True
    i=2
    while i<=math.sqrt(n):
        if not (n%i):
            return False
        i+=1
    return True

def primes_count(n):
    a,i=[],2
    while len(a)<n:
        if primes_checker(i):
            a.append(i)
        i+=1
    return a

def red(a):
    return reduce(lambda a,c:a*c,a)

def solver(k,n,d):
    a,b,c=primes_count(k+n)[k-1:k-1+n],[],[]
    for i in range(n):
        b.append(a[i]**(i+1))
        c.append(a[i]**(n-i))
    return convert(red(b),d),convert(red(c),d)

print(solver(20,4,36))
print(solver(2,2,8))