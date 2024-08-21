from functools import reduce
from operator import mul
from collections import Counter
from itertools import product

def get_num(a):
    d=sorted(map(lambda x:reduce(mul,x),product(*[[j**i for i in range(k+1)] for j,k in Counter(a).items()])))[1:]
    return [reduce(mul,a),len(d),d[0],d[-2]]