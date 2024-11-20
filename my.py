from math import comb

def est_subsets(a):
    n=len(set(a))
    return sum(comb(n,i) for i in range(1,n+1))

print(est_subsets(['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 'd', 'j', 'j', 'n', 'm', 'm']))