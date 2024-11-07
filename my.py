def reverse(a):
    r,i=[[a[0]]],1
    for i in range(1,len(a)):
        t=[a[i]]
        k=len(r[-1])-1
        while k>=0:
            t.insert(0,r[-1][k]-t[0])
            k-=1
        r.append(t)
    return r[-1]

print(reverse([84, 42, 21, 10, 2]))