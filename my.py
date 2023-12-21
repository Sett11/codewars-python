def put_the_cat_on_the_table(c,a):
    x,y=c
    if x<0 or x>=len(a) or y<0 or y>=len(a[0]):
        return 'NoCat'
    z=max([[(i,j) for j,k in enumerate(r) if a[i][j]] for i,r in enumerate(a)])
    if not z:
        return 'NoTable'
    d,e=z[0]
    return 'D'*(d-x)+'U'*(x-d)+'R'*(e-y)+'L'*(y-e)
        
    

print(put_the_cat_on_the_table([0,1],[[0,0,0], [0,0,0], [0,0,1]]))