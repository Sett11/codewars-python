from math import ceil

def e(n):
    r=[True]*n
    r[0]=r[1]=False

    for i in range(2,int(n**.5+1)):
        if r[i]:
            r[2*i:n:i]=[False]*ceil((n/i)-2)
    
    return [i for i,j in enumerate(r) if j]

primes=e(1000000)

def left(n):
    l,r=0,len(primes)

    while r-l>1:
        m=(l+r)//2
        if primes[m]<n:
            l=m
        else:
            r=m
    
    return l+1

def right(n):
    l,r=0,len(primes)

    while r-l>1:
        m=(l+r)//2
        if primes[m]<=n:
            l=m
        else:
            r=m
    
    return r

def bs(n):
    return n in primes[left(n):right(n)]


def find_emirp(n):
    a=[i for i in primes[:left(n)] if str(i)!=str(i)[::-1] and bs(int(str(i)[::-1]))]
    return [len(a),a[-1],sum(a)]


print(find_emirp(20000))