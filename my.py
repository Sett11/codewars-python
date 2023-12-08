from math import ceil

def generate_primes(n):
    if n<2:
        return []
    n+=1
    r=[True]*n
    r[0]=r[1]=False
    for i in range(2,int(n**.5+1)):
        if r[i]:
            r[2*i:n:i]=[False]*ceil((n/i)-2)
    return [i for i,j in enumerate(r) if j]

print(generate_primes(47))