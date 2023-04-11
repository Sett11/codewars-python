def keep_order(a,n):
    i=0
    while i<=len(a):
        if(i==len(a)):
            return i
        if(a[i]>=n):
            return i
        i+=1

print(keep_order([1, 2, 3, 4], 5))