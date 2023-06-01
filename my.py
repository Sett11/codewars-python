def count_odd_pentaFib(n,a=[0,1,1,2,4,8]):
    if(len(a)>=n):
        return len(set([i for i in a[:n+1] if i&1]))
    while(len(a)<=n):
        a.append(sum(a[-5:]))
    return len(set([i for i in a if i&1]))
    

print(count_odd_pentaFib(10))
print(count_odd_pentaFib(7))
print(count_odd_pentaFib(68))