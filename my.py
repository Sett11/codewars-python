def silly_birds(s,c):
    def f(arr,n):
        if not n:
            return [''.join(i) for i in arr]
        l,a=len(arr[0]),[i.copy() for i in arr]
        for i in range(2):
            for j in range(l):
                if i==0:
                    if arr[0][j]=='B':
                        if j==l-1:
                            if arr[1][j-1]=='B' or arr[0][j-2]=='B':
                                a[0][j]='_'
                            else:
                                a[1][j-1],a[0][j]='B','_'
                        elif j==0:
                            if arr[1][j+1]=='B':
                                a[0][j]='_'
                            else:
                                a[1][j+1],a[0][j]='B','_'
                        else:
                            if arr[1][j+1]=='B':
                                if arr[1][j-1]=='B':
                                    a[0][j]='_'
                                else:
                                    a[0][j],a[1][j-1]='_','B'
                            else:
                                a[1][j+1],a[0][j]='B','_'
                else:
                    if arr[1][j]=='B':
                        if j==l-1:
                            if arr[0][j-1]=='B' or arr[1][j-2]=='B':
                                a[1][j]='_'
                            else:
                                a[0][j-1],a[1][j]='B','_'
                        elif j==0:
                            if arr[0][j+1]=='B':
                                a[1][j]='_'
                            else:
                                a[0][j+1],a[1][j]='B','_'
                        else:
                            if arr[0][j+1]=='B':
                                if arr[0][j-1]=='B':
                                    a[1][j]='_'
                                else:
                                    a[1][j],a[0][j-1]='_','B'
                            else:
                                a[0][j+1],a[1][j]='B','_'
        return f(a,n-1)
    return f([list(i) for i in s],c.count('Bang!'))

print(silly_birds(
    ['_B__BB___B_',
     '_BBB___BB__'], 'Bang!Bang!'),sep='\n')