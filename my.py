from functools import reduce
from operator import mul,eq

def vector_op(f, *vs):
   return [f(i) for i in zip(*vs)]
    
def iter_mult(*xs):
   return reduce(mul,list(xs[0]),1)
    
def iter_eq(*xs):
   return reduce(eq,list(xs[0]))

print(vector_op(iter_eq,[1,2,3],[1,2,3]))