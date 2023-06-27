def snakes_and_ladders(l,a):
    i,j=0,0
    while i<len(a):
        if j+a[i]<len(l):
            j+=a[i]
        if l[j]:
            j+=l[j]
        i+=1
    return j
        

print(snakes_and_ladders([0, 0, 3, 0, 0, 0, 0, -2, 0, 0, 0],[2, 1, 5, 1, 5, 4]))
print(snakes_and_ladders( [0, 0, 0, 0, 1, 0, 0, 5, 0, 0, 0, -1, 0, 0],[3, 3, 6, 5, 4, 5]))