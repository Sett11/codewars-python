def path_finder(m):
    l=[list(i) for i in m.split('\n')]
    s,e=set(),len(l)-1
    if not e:
        return True
    s.add(','.join([str(i) for i in [0,0]]))
    while len(s):
        p=[int(i) for i in s.pop().split(',')]
        x,y=p[0],p[1]
        l[x][y]='&'
        t=[i for i in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] if i[0]>-1 and i[1]>-1 and i[0]<=e and i[1]<=e]
        for i in t:
            if i[0]==e and i[1]==e:
                return True
            v=l[i[0]][i[1]]
            if v!='&' and v!='W':
                s.add(','.join([str(j) for j in i]))
    return False

print(path_finder("\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])))
print(path_finder("""......W....W..WWW.W...W.WW.WW..WW..W..WW....W
...W......WWW..W...W....W....W......W........
......W...............WW.....WW...W.W...W....
..W......W..W..WWW..W....W.W..W........W..W..
W.W.W....W............WW.....W.....W......W..
WW..W.WW...W..W....W...W.......W..W..........
....W.W..W..W................W..............W
....W....W....W.......W..........W..WW.....W.
......W..W....W.WW...WW.......WW....W..W..W..
...W............W..W...W....W.W......W.W....W
W.WW.....W...WWWW.....WWW...W.....W..........
.W.WW..W..W..........WWW........W.........W..
W.W.W....WW......WWWW...W..W......W..W..WW.W.
............WW.W.W.W.....W.W...W....W....W...
.WW...W.....W..............W.W....WW.W.......
WWW....W...W.W...W.......WW....W....W...WW...
.W...W.WW.W.W...WW..W..W..WW.................
W...W......WW........W...W....W..............
.WW.WW.........W......W.W...W........W..WW.W.
...WW.W.W........W........W.WWW...W.W.W.W..W.
..W..WW......W.......WW...W...WWWW..W.......W
.WWW..W..W......W.W..WW.WW.WW........W.......
..W.WW.WWW..W.WW.W...W.WW....W...............
......W......W.......WW.............W......W.
WWW...W.............W.......W.W....W.....WWW.
.WW...WWW..............WW....W.W....W..W...W.
WWW..W.W.........................W..W.......W
.W.WWWW...W.......W...W.W.W.W.........W.W.W..
.W.....WW..WWWW..W..WW...W........WWWW.WW.W..
.....WW......W....W.....WW....W.....W.......W
.W.W....W...WW..W.....WW.............WWW.....
...WW..W.W.W.WW......W.......W....WWW..WW.W.W
..........W....W........W.W....WWW.W...W.W.W.
W.....W.WW...W...W.WWW...WWWWW...WW.W.W..WW..
..WWW..W...WW.......WW..W....W.W...W.........
WW.W.W...W...W.W.W..WW..W...........W.W.W....
.W....WW.W.....W.W.WW.WW.....WWW..W........W.
........W..W...W..W........WWW..W.W....W.W.W.
.WWWW...WW....W..W.W.........WWW.......W.....
.........W..W..W...W......W....W..WWW.W......
W...W....W............W.....W..W...W..WW....W
WW.W....W.WW...........W......W..W....WW.W.W.
......W.W.W..W.W.W.WW........WW..........W...
W....W..W..WWW...W.W..W.....W....W.W.....W.W.
WWW.............W...W.W....W......W.........."""))