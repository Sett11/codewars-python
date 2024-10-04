import gmpy2
from collections import Counter
from bisect import bisect

def e(n):
    l=gmpy2.isqrt(n)+1
    n+=1
    b=gmpy2.xmpz(3)
    b[4:n:2]=-1
    for i in b.iter_clear(3,l):
        b[i*i:n:i+i]=-1
    return list(b.iter_clear(2,n))

primes=e(int(5e6))

def f(n):
    c=lambda x:(sum(j for i,j in Counter(str(x)).items() if int(i)%2==0),x)
    g=bisect(primes,n-1)
    return max([c(i) for i in primes[:g]])[1]

print(f(1000))