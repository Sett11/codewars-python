import gmpy2
import bisect

def e(n):
    l=gmpy2.isqrt(n)+1
    n+=1
    b=gmpy2.xmpz(3)
    b[4:n:2]=-1
    for i in b.iter_clear(3,l):
        b[i*i:n:i+i]=-1
    return list(b.iter_clear(2,n))

primes=list(filter(lambda x:all(gmpy2.is_prime(int(y)) for y in str(x)),e(int(1e7))))

def get_total_primes(a,b):
    return len(primes[bisect.bisect_left(primes,a):bisect.bisect_right(primes,b-1)])

print(get_total_primes(10,100))
print(get_total_primes(500,600))

