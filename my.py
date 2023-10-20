from functools import reduce
from operator import mul

def per(n):
    r=[]
    while n>9:
        n=reduce(mul,map(int,list(str(n))))
        r.append(n)
    return r


print(per(277777788888899))
print(per(8))