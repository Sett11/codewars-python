def count_attacking_rooks(a):
    b, u = [[0]*8 for _ in range(8)], set()

    for i in a:
        b[i[0]][i[1]]=1

    def deep_search(i, j):
        nonlocal u
        x,y=i+1,j

        while x<8:
            if b[x][y]==1:
                u.add(tuple(sorted([(i,j),(x,y)])))
                break
            x+=1

        x=i-1

        while x>=0:
            if b[x][y]==1:
                u.add(tuple(sorted([(i,j),(x,y)])))
                break
            x-=1

        x,y=i,j+1

        while y<8:
            if b[x][y]==1:
                u.add(tuple(sorted([(i,j),(x,y)])))
                break
            y+=1

        y=j-1

        while y>=0:
            if b[x][y]==1:
                u.add(tuple(sorted([(i,j),(x,y)])))
                break
            y-=1

    for i,j in a:
        deep_search(i,j)

    return len(u)
    

print(count_attacking_rooks([[2, 5], [5, 3], [5, 5]]),sep='\n')