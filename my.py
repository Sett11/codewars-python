def merge(a):
    n=len(a)
    for i in range(n):
        if not a[i]:
            for j in range(i+1,n):
                if a[j]:
                    a[i],a[j]=a[j],a[i]
                    break
            else:
                break
        for j in range(i+1,n):
            if a[j] and a[i]!=a[j]:
                break
            if a[i]==a[j]:
                a[i]*=2
                a[j]=0
                break
    return a

print(merge([4, 4, 16, 16, 0, 32, 8, 16, 4, 32]))