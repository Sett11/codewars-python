from math import factorial as f
from collections import Counter
from functools import reduce
from operator import mul

def proc_arr(a):
    a.sort()
    return [f(len(a))//reduce(mul,map(f,Counter(a).values())),int(''.join(a)),int(''.join(a[::-1]))]
    
print(proc_arr(['0', '5', '3', '0', '4', '3', '2']))