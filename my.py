FUNCTION={'f3' : lambda n: n*(n + 1)/2, 'f4' : lambda n: n**2, 'f5' : lambda n:n*(3*n - 1)/2, 'f6' : lambda n: n*(2*n - 1), 'f7' : lambda n: n*(5*n - 3)/2, 'f8' : lambda n: n * (3 * n - 2)}

def make_sum_chains(f,n):
    a,r,s=[f(i) for i in range(1,n+1)],[k for k in zip(*[[FUNCTION[j](i) for i in range(1,n+1)] for j in FUNCTION])],0
    for i in range(len(a)):
        s+=(sum(r[i])-a[i])*a[i]
    return s

print(make_sum_chains(FUNCTION['f4'],20))
