from functools import reduce as r
from math import lcm

def kiyo_lcm(a):
    return r(lcm,[sum(j for j in i if isinstance(j,int) and j&1) for i in a])

print(kiyo_lcm([[1, 1, 5, 4, 4, 2, 5, 1, 5], [4, 2, 3, 5, 1, 4, 4, 2, 5], [4, 2, 1, 4, 5, 5, 4, 3, 3], 
             [2, 1, 5, 1, 1, 1, 1, 2, 4], [5, 1, 3, 1, 3, 2, 4, 2, 1], [3, 1, 1, 2, 4, 2, 5, 3, 5], 
             [5, 2, 5, 3, 3, 4, 3, 4, 1], [3, 4, 4, 5, 5, 5, 5, 4, 5], [3, 3, 5, 5, 3, 3, 3, 5, 2]]))