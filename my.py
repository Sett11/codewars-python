def add_all(l):
    r=0
    while len(l)>1:
        a,b=l.pop(l.index(min(l))),l.pop(l.index(min(l)))
        r+=a+b
        l.append(a+b)
    return r

print(add_all([1,2,3,4]))