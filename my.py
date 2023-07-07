def quicksort(a):
    i=0
    while i<len(a):
        j=i+1
        while j<len(a):
            if a[i]>a[j]:
                t=a[i]
                a[i]=a[j]
                a[j]=t
                i=0
                j=0
            j+=1
        i+=1
    return a

print(quicksort([3, 0, 7, 5, 1, 2, 9, 8, 4, 6]))