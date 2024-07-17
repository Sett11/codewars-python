from gmpy2 import is_prime

def lucas_lehmer(n):
    return is_prime(2**n-1)


print(lucas_lehmer(11213))