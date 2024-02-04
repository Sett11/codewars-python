def f(a,n,c):
    for i in range(5,-1,-1):
        if a[i][n]=='-':
            a[i][n]=c
            return a

def connect_four_place(a):
    r=[['-']*7 for _ in range(6)]
    for i,j in enumerate(a):
        f(r,j,'R' if i&1 else 'Y')
    return r

print(connect_four_place([0,1,0,1,0,1]))