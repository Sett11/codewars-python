def sect_sort(a,s=0,e=0):
    i=0
    r=[]
    if(not e):
        e=len(a)
    while i<len(a):
        if(i<s or i>=s+e):
            r.append(a[i])
        else:
            t=sorted(a[s:s+e])
            r.extend(t)
            i+=e-1
        i+=1
    return r

print(sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 8, 3))