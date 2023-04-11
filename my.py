def cleaned_counts(a):
    m=0
    r=a.copy()
    for i in range(len(r)):
        m=max(m,r[i])
        if(r[i]<m):
            r[i]=m
    return r

print(cleaned_counts([5, 5, 6, 5, 5, 5, 5, 6]))