from functools import reduce as r
from operator import mul

p=[2,3,5,7,11,13,17,19,23]

def find_max(n):
    u,m=set([n]),n
    while 1:
        n=r(mul,[p[int(i)-1] if int(i)>0 else 1 for i in list(str(n))])
        if(n not in u):
            u.add(n)
            m=max(m,n)
        else:
            break
    return m

print(find_max(218294180898))