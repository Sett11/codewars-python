from itertools import combinations as c
from functools import reduce as r
from operator import mul as m

def find_min_max_product(a,k):
    if len(a)>=k:
        x=sorted(r(m,i) for i in c(a,k))
        return x[0],x[-1]

print(find_min_max_product([1, -2, -3, 4, 6, 7],3))