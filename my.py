import math
def f(e):
    if(e<2):return False
    if(e==2):return True
    i=2
    while i<math.sqrt(e)+1:
        if(e%i)==0:return False
        i+=1
    return True
def sum_primes(l,u):
    return sum(filter(f,(range(l,u+1))))

print(sum_primes(20,4))