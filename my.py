from itertools import combinations as c

def solve(n,k):
    s=str(n)
    return sorted([''.join(i) for i in c(s,len(s)-k)],key=int)[0]

print(solve(1284569,2))
print(solve(123056,1))
print(solve(123056,4))