def f(x):
    r,d,i,j=set(),{},0,1
    while i<len(x):
        while j<len(x):
            y=x[i]+x[j]
            r.add(y)
            if y in d:
                d[y]+=1
            else:
                d[y]=1
            j+=1
        i+=1
        j=i+1
    return min(list(filter(lambda e:e not in set(x) and d[e]==1,r)))

def ulam_sequence(a,b,n):
    a=[a,b,a+b]
    while len(a)<n:
        a.append(f(a))
    return a

print(ulam_sequence(5,6,8))