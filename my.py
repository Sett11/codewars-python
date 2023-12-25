from functools import lru_cache

@lru_cache
def perm(a):
    n=len(a)
    if n<2:
        return a
    t,p,r=perm(a[1:]),a[0],[]
    for i in t:
        for j in range(n):
            r+=[i[0:j]+p+i[j:]]
    return r

def nth_perm(n,d):
    return sorted(perm(''.join(str(i) for i in range(d))))[n-1]

print(nth_perm(12,5))