def yoga(a,p):
    r,c=[sum(i) for i in a],0
    for i in range(len(p)):
        for j in range(len(a)):
            c+=sum([1 for k in a[j] if k+r[j]>=p[i]])
    return c

print(yoga([
                    [7,2,1,0],
                    [1,3,2,2],
                    [1,9,1,2],
                    ],[1000,20,3,105,66,204,4,1, 22, 86]))