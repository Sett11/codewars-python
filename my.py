def cartesian_neighbor(x,y):
    a=[]
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            a.append((i,j)) if (i,j)!=(x,y) else None
    return a

print(cartesian_neighbor(5,7))