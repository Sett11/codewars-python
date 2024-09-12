def dice_game(a):
    print(a)
    k,r,i=4,['p1','p2','p3','p4'],0
    while i<len(a):
        if len(r)==1:
            return r[0]
        q=a[i:i+k]
        i+=k
        w=sorted(q,key=sum)
        if len([i for i in w if sum(i)==sum(w[0])])==1:
            j=q.index(w[0])
            r.pop(j)
            k-=1
        else:
            x=sorted([i for i in q if sum(i)==sum(w[0])])
            if len(set(x))!=len(x):
                continue
            else:
                j=q.index(x[0])
                r.pop(j)
                k-=1
    return r[0]


print(dice_game([(6, 2), (4, 4), (6, 1), (4, 4), (3, 3), (3, 4), (1, 2), (3, 2), (5, 3), (4, 5), (4, 4), (2, 2), (4, 5), (4, 5), (3, 2), (5, 1), (2, 3), (6, 1)]))