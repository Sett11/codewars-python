def or_arrays(a1,a2,v=0):
    m,n=len(a1),len(a2)
    if m<n:
        a1+=[v]*(n-m)
    if n<m:
        a2+=[v]*(m-n)
    return [a1[i]|a2[i] for i in range(len(a1))]


print(or_arrays([1,2,3],[4,5,6]))
print(or_arrays([1,2,3],[1,2]))