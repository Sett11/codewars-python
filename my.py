def bubblesort_once(l):
    l=l.copy()
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            t=l[i]
            l[i]=l[i+1]
            l[i+1]=t
        i+=1
    return l

print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]))