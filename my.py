def merge(a,w,l,m,r):
    t,i,j=[],l,m+1
    while i<m+1 and j<=r:
        if a[i][0]>a[j][0]:
            w[a[i][1]]+=r-j+1
            t.append(a[i])
            i+=1
        else:
            t.append(a[j])
            j+=1
    while i<=m:
        t.append(a[i])
        i+=1
    while j<=r:
        t.append(a[j])
        j+=1
    k,i=0,l
    while i<=r:
        a[i]=t[k]
        i+=1
        k+=1

def merge_sort(a,r,i,j):
    if i<j:
        m=(i+j)//2
        merge_sort(a,r,i,m),merge_sort(a,r,m+1,j),merge(a,r,i,m,j)

def smaller(a):
    n=len(a)
    v,r=[[a[i],i] for i in range(n)],[0]*n
    merge_sort(v,r,0,n-1)
    return r

print(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]))