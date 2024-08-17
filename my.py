from functools import reduce
from operator import mul
from collections import Counter

def product_sans_n(a):
    c,n,u=Counter(a),reduce(mul,list(filter(lambda e:e,a)),1),set(a)
    if(c[0]>1):return [0]*len(a)
    for i in c:
        c[i]=n//i if i else n
    return [c[i] if 0 not in u else n if not i else 0 for i in a]

print(product_sans_n([6, 3, 4, 6, 6, -5, -2, -5, 4, 4, -1, 4, -4, 2, 4, -2, -3, 1, 5, 2, -7, 7, 7, 7, -3, -2, 7, 5, -6, 4, 7, 7, 1, 5, 1, 2, 7, 3, 6, 4, 5, 5, 2, 3, -7, 6, -2, 1, -5, 7, 5, 4, 1, 2, -7, -3, 2, 6, 5, 7, 6, 5, 5, 7, 4, 7, -1, -6, -5, 5, 1, 2, 1, -4, 7, 6, 3, -7, 4, 6, 3, 5, 1, 5, -2, 4, 5, 2, 5, 2, 4, 7, 3, -4, 7, 3, 5, 6, 3, 3, 1, 6, -5, 3, -5, 6, -1, -5, 3, 1, 1, 4, 5, 2, 2, -6, 3, 2, 7, -5, -7, 4, 5, 7, 1, 5, 2, -5, -7, 2, 5, 5, 4, 5, 6, 5, -5, 1, 7, 6, 3, 1, 2, 2, 4, -1, 1, 2, -2, 1, 2, 3, 4, 7, 3, 7, 3, -4, -4, 6, 7, -3, 3, -3, 7, -7, -6, 6, 1, 1, 5, 6, -1, -6, 5, -6, 7, 4, 5, -6, 3, 5, 5, 5, 5, 3]))