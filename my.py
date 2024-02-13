from functools import reduce as r
from math import lcm

def mn_lcm(m,n):
    print(m,n)
    return r(lcm,range(min(m,n),max(m,n)+1))