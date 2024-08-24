from collections import Counter
from functools import reduce
from operator import mul
from math import factorial as f
from decimal import Decimal as D

def list_position(w):
    s,c=sorted(w),1
    for i in w:
        if i==s[0]:
            s.pop(0)
            continue
        t=s.index(i)
        c+=(t*D(f(len(s)-1)/reduce(mul,map(f,Counter(s).values()))))
        s.pop(t)
    return int(c)

print(list_position('IMMUNOELECTROPHORETICALLY'))