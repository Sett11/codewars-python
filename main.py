from itertools import compress
from math import isqrt

def primes(n):
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

primes_list = primes(isqrt(10000000000000000))

def factorization(n):
    pf = []
    for p in primes_list:
      if p*p > n:
        break
      count = 0
      while n % p == 0:
        n //= p
        count += 1
      if count > 0:
        pf.append((p, count))
    if n > 1:
        pf.append((n, 1))
    return pf

def divisor(n):
    divs = set([1])
    for p, e in factorization(n):
        divs.update([x*p**k for k in range(1,e+1) for x in divs])
    return sorted(divs)

print(divisor(9999999999999994))