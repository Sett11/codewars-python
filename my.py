def find_treasure(a,x,y):
    x,y=x-1,y-1
    while True:
        i,j=map(lambda z:int(z)-1,list(str(a[x][y])))
        if (i,j)==(x,y):
            return int(str(i+1)+str(j+1))
        x,y=i,j

print(find_treasure([ [34,21,32,44,25], [21,41,43,14,31], [31,45,52,42,23], [33,15,51,44,35], [21,52,33,13,44] ],3,4))