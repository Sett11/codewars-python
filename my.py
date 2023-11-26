def rotate_corners(a):
    f=lambda x: ord(x) if isinstance(x,str) else int(x) if isinstance(x,bool) else x
    n,m=len(a),len(a[0])
    r=[[a[0][0],a[0][m-1]],[a[n-1][0],a[n-1][m-1]]]
    a[0][0]=a[0][m-1]=a[n-1][0]=a[n-1][m-1]=0
    k=(sum(map(f,sum(r,[])))*sum(map(f,sum(a,[]))))%4

    while k:
        r=[list(i)[::-1] for i in zip(*r)]
        k-=1
    
    return r

print(rotate_corners([['!', ':', 7, '^'], [997, 'T', '<', '+'], [47, 'v', 531, 'Q'], ['{', '[', ']', '}']]))