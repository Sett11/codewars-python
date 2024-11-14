from gmpy2 import is_prime

def is_carmichael(n):
    if n%2==0 or n<2 or is_prime(n):
        return False
    for i in range(2,int(n**.5)):
        if pow(i,n,n)!=i:
            return False
    return True

print(is_carmichael(5323))