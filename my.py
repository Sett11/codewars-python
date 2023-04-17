def sort_by_height(a):
    b=list(map(lambda e:'&' if e!=-1 else e,a));c=sorted(list(filter(lambda e:e>-1,a)))
    for i in range(len(b)):
        if(b[i]=='&'):
            b[i]=c.pop(0)
    return b

print(sort_by_height([-1, 150, 190, 170, -1, -1, 160, 180]))