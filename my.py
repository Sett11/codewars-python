import gmpy2

def e(n):
    l=gmpy2.isqrt(n)+1
    n+=1
    b=gmpy2.xmpz(3)
    b[4:n:2]=-1
    for i in b.iter_clear(3,l):
        b[i*i:n:i+i]=-1
    return list(b.iter_clear(2,n))

def channelling_primes(n):
    return sum(map(lambda x:2**(x-1),e(n)))

print(channelling_primes(21))