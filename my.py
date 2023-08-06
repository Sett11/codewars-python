from itertools import permutations as p
from math import sqrt
def next_perfectsq_perm(l,k): 
    i=int(sqrt(l)+1)
    while 1:
        s=str(i**2)
        t=[q for q in set([int(''.join(j)) for j in p(s) if '0' not in s]) if sqrt(q)==int(sqrt(q))]
        if len(t)==k:
            return max(t)
        i+=1

print(next_perfectsq_perm(3550000,5))