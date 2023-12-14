from itertools import product

def comfortable_numbers(l,r):
    a=[i for i in range(r+1)]
    q=set()
    for i in range(l,r):
        s=sum(map(int,str(a[i])))
        q.update([k for k in product([a[i]],[j for j in a[a[i]:a[i]+s+1] if j>=l and j<=r and j!=a[i]]) if k[0] in list(range(k[1]-sum(map(int,str(k[1]))),k[1]+1+sum(map(int,str(k[1])))))])
    return len(q)

print(comfortable_numbers(1,1000))