from functools import reduce as r
import math as m

def get_dividers(v,p):
    a=[]
    for i in range(len(v)):
        a.append(v[i]**p[i])
    a=r(lambda a,c:a*c,a)
    c=[]
    for i in range(1,int(m.sqrt(a))):
        if(a%i==0):
            c.append(int(i))
            c.append(int(a/i))
    return sorted(c)

print(get_dividers([2, 5, 11], [2, 1, 1]))