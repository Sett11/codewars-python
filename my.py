from functools import reduce
from operator import mul

def strong_enough(a,n):
    return ["Needs Reinforcement!",'Safe!'][reduce(mul,map(sum,a))<=1000*pow(.99,n)]

print(strong_enough([[5,1,7],[1,1,1],[4,1,2]],100))
print(strong_enough([[5,1,7],[1,1,7],[4,1,2]],50))