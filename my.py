def shake_tree(t):
    n,m=len(t),len(t[0])
    r=[0]*m
    def f(i,j):
        while i<n:
            while t[i][j]=='\\':
                j+=1
                if t[i][j]=='/':
                    return -1
            while t[i][j]=='/':
                j-=1
                if t[i][j]=='\\':
                    return -1
            if t[i][j]=='_' or (i!=n-1 and t[i+1][j]=='_'):
                return -1
            i+=1
        return j
    for i in range(n):
        for j in range(m):
            if t[i][j]=='o':
                k=f(i,j)
                if k!=-1:
                    r[k]+=1
    return r

print(shake_tree([' o      ',
                  ' / o o/ ',
                  ' \\//    ',
                  '   \\//  ',
                  '   ||   ',
                  '   ||   ',
                  '   ||   ']))
print(shake_tree([" o      ",
                " / o o/ ",
                " ///    ",
                "   ///  ",
                "   ||   ",
                "   ||   ",
                "   ||   "]))