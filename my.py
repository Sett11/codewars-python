def find_similar_dogs(s):
    a,r,m=set(dogs[s]),{},0
    for i in dogs:
        if i!=s:
            l=len(a&set(dogs[i]))
            if l not in r:
                r[l]=set()
            r[l].add(i)
            m=max(m,l)
    return r[m]