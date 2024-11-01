from math import factorial as f
from functools import reduce
from operator import mul
from collections import Counter

def uniq_count(s):
    return f(len(s))//reduce(mul,map(f,Counter(s.lower()).values())) if s else 1

print(uniq_count('ABBb'))