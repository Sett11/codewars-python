def split_workload(l):
    a=[]
    i=0
    while i<len(l):
        a.append((i,abs(sum(l[i:])-sum(l[:i]))))
        i+=1
    return min(a,key=lambda e:e[1]) if len(l) else (None,None)

print(split_workload([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0, 2, 3, 4, 5, 6, -4, -3, -2, -1, 0, 1, -1, 0, 1, 2, 3, -7, -6, -5, -4, -3, -2, 0, 1, 2, 3, 4, -6, -5, -4, -3, -2, -1]))