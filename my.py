from itertools import permutations
from functools import reduce

def check(a,b):
    return a and b and min(a)>min(b) and max(a)<max(b)

def matryoshka(lst):
    a=[list(i) for i in permutations(lst)]
    for i in a:
        if reduce(lambda x,y:x+y if check(x,y) else [],i):
            return True
    return False

print(matryoshka([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6], [4, 5]]))