from functools import reduce
from operator import mul

def find_us(n1, n2, k, pf, d):
    return [i for i in range(reduce(mul,pf),n1+k*n2,max(pf)) if all(i%j==0 for j in pf) and all(str(j) in str(i) for j in d)]


print(find_us(30, 90, 4, [2, 3], [6, 2]))
print(find_us(30, 400, 18, [2, 3, 7], [6, 2, 5]))
print(find_us(230,7059,435,[2, 17, 7, 29],[5, 3, 2, 6]))