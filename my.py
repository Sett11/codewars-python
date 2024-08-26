def spiralize(n):
    a,d,s,i,j=[[0]*n for _ in range(n)],{'right':lambda x,y:(x,y+1),'down':lambda x,y:(x+1,y),'left':lambda x,y:(x,y-1),'up':lambda x,y:(x-1,y)},'right',2,1
    a[0],a[-1]=[1]*n,[1]*n
    for k in range(n):
        a[k][-1]=1
        if k>1:
            a[k][0]=1
    while True:
        v=False
        if s=='right' and a[i][j+1]==1:
            s,v='down',True
            j-=1
        elif s=='down' and a[i+1][j]==1:
            s,v='left',True
            i-=1
        elif s=='left' and a[i][j-1]==1:
            s,v='up',True
            j+=1
        elif s=='up' and a[i-1][j]==1:
            s,v='right',True
            i+=1
        if not v:
            a[i][j]=1
            i,j=d[s](i,j)
        else:
            i,j=d[s](i,j)
            if ((s=='left' or s=='right') and (a[i-1][j]==1 or a[i+1][j]==1)) or\
               ((s=='down' or s=='up') and (a[i][j-1]==1 or a[i][j+1]==1)) or\
               (a[i+1][j]==1 and a[i-1][j]==1) or (a[i][j+1]==1 and a[i][j-1]==1):
                break
            else:
                a[i][j]=1
    return a
 
print(*spiralize(15),sep='\n')