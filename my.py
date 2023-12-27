def finaldist_crazyrobot(a,p):
    x,y=p
    for i,j in a:
        i=i.lower()
        if i=='r':
            x+=j
        elif i=='l':
            x-=j
        elif i=='u':
            y+=j
        else:
            y-=j
    return ((x-p[0])**2+(y-p[1])**2)**.5


print(finaldist_crazyrobot([('R', 2), ('U', 3), ('L', 1), ('D', 6)],(0,0)))