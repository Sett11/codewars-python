import math

def all_squared_pairs(n):
    a,c=[],math.ceil(math.sqrt(n))
    for i in range(c):
        nx=i**2
        ny=n-nx
        y=math.sqrt(ny)
        if y>=i and y%1==0:
            a.append([i,y])
    if not n:
        a.append([0,0])
    return a



print(all_squared_pairs(325))
print(all_squared_pairs(1048039120))