from itertools import groupby

def rank(a):
    r,d,k=[list(j) for _,j in groupby(sorted(a))],{},0
    for i in r:
        n=len(i)
        d[i[0]]=sum(range(k,k+n))/n
        k+=n
    return [d[i] for i in a]

print(rank([1, 2, 0, 3, 7, 1, 11, 1, 2]))