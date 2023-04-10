def in_asc_order(a):
    i=0
    while i<len(a)-1:
        if(a[i]>a[i+1]):
            return 1==2
        i+=1
    return 1==1

print(in_asc_order([1,2,4,7,19]))