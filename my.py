def repeat_sum(l):
    l=list(map(set,l))
    a=[];b=[]
    for i in l:
        for j in i:
           if(a.count(j)==0):
               a.append(j)
           else:
               b.append(j)
    return sum(set(b))

print(repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]))