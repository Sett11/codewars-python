def borda_count(a):
    d={i:0 for i in set(sum([a[i] for i in a],[]))}
    n=len(d)
    for i in a:
        for j,k in enumerate(a[i]):
            d[k]+=n-j-1
    s=sum(d.values())/n
    u={i for i in d if d[i]<s}
    if len(u)==n:
        return u
    if not u:
        return {*d.keys()}
    for i in a:
        for j in u:
            del a[i][a[i].index(j)]
            if len(a[i])==1:
                return {a[i][0]}
    return borda_count(a)


print(borda_count( {
'A': ['a', 'b'],
'B': ['b', 'a']
}))