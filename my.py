def snake_collision(board,moves):
    r,n,m,a=moves.split(),len(board),len(board[0]),[list(i) for i in board]
    if not r or all(i.isalpha() for i in r):
        return (0,2),0
    dir,cd,count,snake,i,j='R',int(r.pop(0) if r[0].isdigit() else 0),0,[(0,0),(0,1),(0,2)],0,2
    if len(r)&1:
        r.append('0')
    r=[(r[i],r[i+1]) for i in range(0,len(r),2)]
    l=len(r)
    while l>=0:
        while cd:
            if dir=='R':
                if j==m-1 or a[i][j+1] not in '-$':
                    return (i,j),count+1
                else:
                    if a[i][j+1]=='-':
                        for x in range(len(snake)-1):
                            t=snake[x]
                            a[t[0]][t[1]]='-'
                            snake[x]=snake[x+1]
                        j+=1
                        snake[-1]=i,j
                        for x,y in snake:
                            a[x][y]='o'
                    else:
                        j+=1
                        snake.append((i,j))
                        a[i][j]='o'
            elif dir=='L':
                if j==0 or a[i][j-1] not in '-$':
                    return (i,j),count+1
                else:
                    if a[i][j-1]=='-':
                        for x in range(len(snake)-1):
                            t=snake[x]
                            a[t[0]][t[1]]='-'
                            snake[x]=snake[x+1]
                        j-=1
                        snake[-1]=i,j
                        for x,y in snake:
                            a[x][y]='o'
                    else:
                        j-=1
                        snake.append((i,j))
                        a[i][j]='o'
            elif dir=='D':
                if i==n-1 or a[i+1][j] not in '-$':
                    return (i,j),count+1
                else:
                    if a[i+1][j]=='-':
                        for x in range(len(snake)-1):
                            t=snake[x]
                            a[t[0]][t[1]]='-'
                            snake[x]=snake[x+1]
                        i+=1
                        snake[-1]=i,j
                        for x,y in snake:
                            a[x][y]='o'
                    else:
                        i+=1
                        snake.append((i,j))
                        a[i][j]='o'
            elif dir=='U':
                if i==0 or a[i-1][j] not in '-$':
                    return (i,j),count+1
                else:
                    if a[i-1][j]=='-':
                        for x in range(len(snake)-1):
                            t=snake[x]
                            a[t[0]][t[1]]='-'
                            snake[x]=snake[x+1]
                        i-=1
                        snake[-1]=i,j
                        for x,y in snake:
                            a[x][y]='o'
                    else:
                        i-=1
                        snake.append((i,j))
                        a[i][j]='o'
            cd-=1
            count+=1
        if not r:
            break
        t=r.pop(0)
        dir,cd=t[0],int(t[1])
    return (i,j),count

print(snake_collision([
              'ooo------$--$$$------',
              '-----$$$--$--$---$--$',
              '-$-----$--$-$---$----',
              '------$$$----$---$---',
              '--$$--$---------$$---',
              '-----$$---$$$--$$--$-',
              '----$-----$-$----$--$',
              '$-----$-$$---$$---$--',
              '$--------------------',
              '-------$---$------$-$',
              '----$-$$----------$$-',
              '--$-$$$--$-$--$-----$',
              '$------$--$----------'
          ],'8 D 5 L 7 D 6 L 4 D 8 R 3 U 7 R 8 U 1 L 3 U 5 R 2 D 5 R 5 U 1 L 2 U 7 L 7 D 4 R 6 U 6 L 2 D 7 R 3 D 6 L 2 U 3 R 3 U 5 L 5 U 3 L 7 D 7 R'),sep='\n')