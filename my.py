def majority(a):
    a=sorted([[i,a.count(i)] for i in a],key=lambda e:e[1],reverse=True)
    return a[0][0] if len(set(list(map(lambda u:u[0],list(filter(lambda e:e[1]==a[0][1],a))))))==1 else None

print(majority(["A", "B", "A"]))