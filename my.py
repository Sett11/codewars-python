def direction(f,t):
    a=['N','NE','E','SE','S','SW','W','NW']
    n,c=t//45,a.index(f)
    return a[(n+c)%len(a)]

print(direction('S',180))
print(direction('SE',-45))