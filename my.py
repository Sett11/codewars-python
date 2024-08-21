from gmpy2 import is_prime
from itertools import groupby

def simplified_array(a):
    b=[sum(i) for _,i in groupby(a,key=lambda x:is_prime(x) and x>1)]
    return a if a==b else simplified_array(b)

print(simplified_array([-3, 4, 5, 2, 0, -10]))
print(simplified_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))