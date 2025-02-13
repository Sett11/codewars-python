def four_piles(n,y):
    for  i in range(1,n):
        x=[(i+y),(i-y),(i*y),(i/y)]
        if sum(x)==n and all(j for j in x):
            return x
    return []

print(four_piles(48,3))
