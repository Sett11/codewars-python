from random import shuffle

def find_replaced(a):
    a.sort()
    r,i=[0]*2,1
    while i<len(a):
        if a[i]-a[i-1]!=1:
            if a[i]-a[i-1]:
                r[0]=a[i]-1
            else:
                r[1]=a[i]
            if all(j for j in r):
                return tuple(r)
        i+=1

arr=list(range(1,1000))
arr[40]=arr[42]
shuffle(arr)

print(find_replaced(arr))