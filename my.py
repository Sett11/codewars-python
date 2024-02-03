from itertools import product
from functools import reduce

def sum_times_tables(l,a,b):
    return reduce(lambda x,y:x+(y[0]*y[1]),product(range(a,b+1),l),0)

print(sum_times_tables([2,3],1,3))