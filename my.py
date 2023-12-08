def find(a):
    a=sorted(a)
    r=[a[i+1]-a[i] for i in range(len(a)-1)]

    for i in range(len(r)-1):
        if r[i]!=r[i+1]:
            return a[i+1]+(r[i+1]-r[i])
    
    return a[0]

print(find([3, 9, 1, 11, 13, 5]))
print(find([5, -1, 0, 3, 4, -3, 2, -2]))
print(find([1,1,1,1,1,1,1]))