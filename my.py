from itertools import accumulate as acc

def max_sum(a,r):
    ac=list(acc(a))+[0]
    m=float('-inf')
    for i,j in r:
        m=max(m,ac[j]-ac[i-1])
    return m

print(max_sum([1,-2,3,4,-5,-4,3,2,1], [[1,4],[2,5]]))