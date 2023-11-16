from re import sub

def travel_chessboard(s):
    a,b,c,d=map(int,sub(r'\D','',s))
    r=[[0]*9 for _ in range(9)]
    
    r[a-1]=[1]*9

    for i in range(9):
        r[i][b-1]=1

    for i in range(a,9):
        for j in range(b,9):
            r[i][j]=r[i-1][j]+r[i][j-1]
            if [i,j]==[c-1,d-1]:
                return r[i][j]
    
    return 1

print(travel_chessboard("(1 2)(8 7)"))