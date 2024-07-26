def near_flatten(a):
    r=[]
    while a:
        for i in range(len(a)):
            if isinstance(a[i],list) and all(isinstance(j,int) for j in a[i]):
                r.append(a[i])
        a=sum([g for g in a if isinstance(g,list)],[])
    return sorted(r)

print(near_flatten([[1,2,3],[[4,5],[[6],[7,8]]]]))
print(near_flatten([[[1,2,3],[9,10]],[[4,5],[6,7,8]]]))