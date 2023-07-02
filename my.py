def chess_board(r,c):
    a=[]
    for i in range(r):
        t,x,y=[],0,0
        for j in range(c):
            if i%2==0:
                if x%2==0:
                    t.append('O')
                    x+=1
                else:
                    t.append('X')
                    x+=1
            else:
                if y%2==0:
                    t.append('X')
                    y+=1
                else:
                    t.append('O')
                    y+=1
        a.append(t)
    return a

print(chess_board(6,4))