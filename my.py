def identify_bb(a,f):
    n=len(a)
    return a[f(*sum([[a[i]]*(i+1) for i in range(n)],[]))-sum([10*(i+1) for i in range(n)])-1]
