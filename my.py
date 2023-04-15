def hot_singles(a,b):
    r=[]
    x=list(filter(lambda e: e not in b,a))
    x.extend(list(filter(lambda e: e not in a,b)))
    for i in x:
        if(i not in r):r.append(i)
    return r

print(hot_singles([10, 200, 30], [10, 20, 3, 4, 5, 5, 5, 200]))