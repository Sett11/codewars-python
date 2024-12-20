def cup_and_balls(b,arr):
    a=[0 if i!=b else 1 for i in range(1,4)]
    for i,j in arr:
        a[i-1],a[j-1]=a[j-1],a[i-1]
    return a.index(1)+1

print(cup_and_balls(2,[[1,3],[1,2],[2,1],[2,3]]))
print(cup_and_balls(1,[[2,3],[1,2],[1,2]]))