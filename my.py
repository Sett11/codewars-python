def f(x,n):
    for i in x:
        if(i<n):
            return False
    return True

def socialist_distribution(p,m):
    if(sum(p)<m*len(p)):
        return []
    a=[i-m for i in p]
    while not f(p,m):
        i=p.index(min(p))
        j=p.index(max(p))
        p[i]+=1
        p[j]-=1
    return p

print(socialist_distribution([2,3,5,15,75],5))
print(socialist_distribution([2,3,5,45,45],5))
print(socialist_distribution( [8, -2, 41, 21, 8, -3, 21, 11, 29, -4, 24, -2, 21, 1, 48, 40, 36, 34, 10, 32, 16, 28, -1, 9, 28, 23, 26, -9, 10, 44, 41, 24, 12, 46, 36, 14, 3, 23],2))