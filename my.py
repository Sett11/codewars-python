from functools import reduce
import math

def r(a,b):
    return a+b

def is_perfect(n):
    if(n==1):
        return False
    a=[]
    i=1
    while i<math.sqrt(n):
        if(n%i)==0:
            a.append(i)
            if(n/i)<=n/2:
                a.append(n/i)
        i+=1
    return  reduce(r,a)==n

print(is_perfect(28))