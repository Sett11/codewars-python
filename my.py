from itertools import combinations
from math import gcd
from collections import defaultdict

d=defaultdict(int)

def find_int_inrange(a,b):
    global d
    m=0
    for i in range(a,b+1):
        if i not in d:
            t=str(i)
            x=sum(sum([[int(''.join(k)) for k in combinations(t,j)] for j in range(1,len(t))],[])+[int(t)])
            y=sum(map(int,sum([[t[j:j+k] for j in range(len(t)-k+1)] for k in range(1,len(t))]+[[t]],[])))
            z=gcd(x,y)
            c=0
            while z>1:
                if x%z==0 and y%z==0:
                    c+=1
                z-=1
            m=max(m,c)
            d[i]=c
        else:
            m=max(m,d[i])
    return [m]+[i for i in d if d[i]==m and a<=i<=b]

print(find_int_inrange(300,55000))