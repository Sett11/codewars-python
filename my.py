def number_of_clans(d,k):
    a=list(range(1,k+1))
    r=[]
    for i in range(k):
        s=sum(r,[])
        if a[i] in s:
            continue
        t=[a[i]]
        q=[a[i]%p==0 for p in d]
        for j in range(i+1,k):
            if q==[a[j]%p==0 for p in d]:
                t.append(a[j])
        r.append(t)
    return len(r)


print(number_of_clans([2,3],6))