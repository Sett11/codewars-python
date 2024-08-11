def cantor(a):
    return [a[i][i]^1 for i in range(len(a))]

print(cantor([[0,0,0],
        [1,1,1],
        [0,1,0]]))