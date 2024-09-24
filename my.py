def shake_tree(t):
    n,m=len(t),len(t[0])
    r=[0]*m
    def f(i,j):
        while i<n:
            if t[i][j]=='\\':
                j+=1
            if t[i][j]=='/':
                j-=1
            if t[i][j]=='_':
                return -1
            i+=1
        return j
    for i in range(m):
        if t[0][i]=='o':
            j=f(0,i)
            if j!=-1:
                r[j]+=1
    return r

print(shake_tree([" o o o  ",
                  " \\    \\ ",
                "   \\    ",
                "  \\  \\  ",
                "   ||   ",
                "   ||   ",
                "   ||   "]))
print(shake_tree([" o o o  ",
                " /    / ",
                "   /    ",
                "  /  /  ",
                "   ||   ",
                "   ||   ",
                "   ||   "]))