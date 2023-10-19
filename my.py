from itertools import product
from functools import reduce

def solve(a):
    return max([reduce(lambda e,c:e*c,i) for i in product(*a)])

print(solve([[1,-1],[2,3],[10,-100]]))