import math

def prime_factors(n):
    i,a=2,[]
    while i<=n*n:
        while(not (n%i)):
            n//=i
            a.append(i)
        i+=1
    return a

print(prime_factors(12))