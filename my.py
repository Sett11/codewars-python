from itertools import zip_longest as z,product as p
from math import factorial as f

def gta(n,*args):
    r,u=[],set()
    for i in z(*map(str,args)):
        for j in i:
            if j and j not in u:
                r.append(int(j))
                u.add(j)
    r=r[:n]
    l=len(r)
    return sum([sum([sum(j) for j in p(r,repeat=i) if len(set(j))==i]) for i in range(1,l)])+sum(r)*f(l)
    
    

print(gta(6,5522, 6674))