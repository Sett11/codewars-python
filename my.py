def line(a):
    n,m,b,u,u2,u3,v=len(a),len(a[0]),sum([[(i,j) for j,k in enumerate(p) if k=='X'] for i,p in enumerate(a)],[]),set(),set(),set(),False
    f=lambda i,j:[(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<n and 0<=y<m and (x,y) not in u2.union(u) and a[x][y]!=' ']
    u3.update(b)
    
    def dfs(i,j,d):
        nonlocal v
        if (i,j) in b:
            v=True
            return
        u.add((i,j))
        t=f(i,j)
        if a[i][j]!='+':
            if d in 'rl':
                t=[(x,y) for x,y in t if y in (j-1,j+1)]
            else:
                t=[(x,y) for x,y in t if x in (i-1,i+1)]
            if not t:
                return
            t=t[0]
            if (a[t[0]][t[1]]=='-' and d in 'rl') or (a[t[0]][t[1]]=='|' and d in 'ud') or a[t[0]][t[1]] in '+X':
                x,y=t
                dfs(x,y,'u' if x<i else 'd' if x>i else 'r' if y>j else 'l')
            else:
                return
        else:
            if d in 'rl':
                t=[(x,y) for x,y in t if x in (i-1,i+1)]
                if not t or (len(t)>1 and ([1 for x,y in t if a[x][y] not in '+X'] or all(a[x][y]=='+' for x,y in t))):
                    return
                x,y=t[0]
                dfs(x,y,'d' if x>i else 'u')
            else:
                t=[(x,y) for x,y in t if y in (j-1,j+1)]
                if not t or (len(t)>1 and ([1 for x,y in t if a[x][y] not in '+X'] or all(a[x][y]=='+' for x,y in t))):
                    return
                x,y=t[0]
                dfs(x,y,'r' if y>j else 'l')

    for i,j in b:
        u.clear()
        u2.clear()
        u2.add((i,j))
        t=f(i,j)
        for k in range(len(t)):
            x,y=t[k]
            if (y in (j+1,j-1) and a[x][y] not in '-+X') or (x in (i+1,i-1) and a[x][y] not in '|+X'):
                t[k]=0
        t=[k for k in t if k]
        if len(t)>1 or not t:
            continue
        x,y=t[0]
        dfs(x,y,'u' if x<i else 'd' if x>i else 'r' if y>j else 'l')
        u3.update(u)
        if v:
            break
    for i in range(n):
        for j in range(m):
            if a[i][j]!=' ' and (i,j) not in u3:
                return False
    return v

print(line(['   +-----+  ',
            '   |+---+|  ',
            '   ||+-+||  ',
            '   |||X+||  ',
            '   X|+--+|  ',
            '    +----+  ']))
print(line(['    +----+  ',
            '    |+--+|  ',
            '    ||X+||  ',
            '    |+-+||  ',
            '    +---+|  ',
            'X--------+  ']))
print(line(['    +-+    ',
            '    | |    ',
            '    ++++   ',
            '    ++++   ',
            '   X+++    ',
            '     +---X ']))

print(line(['     X        ', '     |   |    ', ' +   |  -+-   ', '     |   |    ', '     X        ']))
print(line(["                      ",
            "   +-------+          ",
            "   |      +++---+     ",
            "X--+      +-+   X     "]))
print(line(["                    ",
            "     +--------+     ",
            "  X--+        +--+  ",
            "                 |  ",
            "                 X  ",
            "                    "]))
print(line(["           ",
                "X---------X",
                "           ",
                "           "]))