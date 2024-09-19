def square_color(a,b):
    bord=[j if i%2 else j[::-1] for i,j in enumerate([['black','white']*4 for _ in range(8)])]
    return bord[-b][ord(a)-97]

print(square_color('a',8))
print(square_color('b',2))