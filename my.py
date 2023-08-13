def f(a,x,y):
    r,i,j=list([i for i in zip(*a)][y])+a[x],x-1,y-1
    while i>-1 and j>-1:
        r.append(a[i][j])
        i-=1
        j-=1
    i,j=x+1,y+1
    while i<len(a) and j<len(a[0]):
        r.append(a[i][j])
        i+=1
        j+=1
    i,j=x+1,y-1
    while i<len(a) and j>-1:
        r.append(a[i][j])
        i+=1
        j-=1
    i,j=x-1,y+1
    while i>-1 and j<len(a[0]):
        r.append(a[i][j])
        i-=1
        j+=1
    return len(r)-2

def chessboard_squares_under_queen_attack(a,b):
    r,s=[list('0'*b) for i in range(a)],0
    for i in range(len(r)):
        for j in range(len(r[i])):
            s+=f(r,i,j)
    return s
    
print(chessboard_squares_under_queen_attack(20,20))