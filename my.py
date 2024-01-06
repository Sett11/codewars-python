from math import lcm
from itertools import product

def d(n):
    s=set()
    for i in range(1,int(n**.5+1)):
        if n%i==0:
            s.update([i,n//i])
    return s

def lcm_cardinality(n):
    a=d(n)
    return len(set(map(lambda e:tuple(sorted(e)),filter(lambda x:lcm(*x)==n and len(set(x))==2,product(a,repeat=2)))))+1

print(lcm_cardinality(30858025))
print(lcm_cardinality(9801))
print(lcm_cardinality(1251562))