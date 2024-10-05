def escape(a):
    x,y=[[(i,j) for j,k in enumerate(p) if k==2] for i,p in enumerate(a) if 2 in p][0][0]
    n,m,r,g=len(a),len(a[0]),[],-1
    a[-1][-1]=1
    while (x,y)!=(n-1,m-1):
            try:
                g=a[x].index(1)
                s=('L' if g<y else 'R' if g>y else 'D')
                k=abs(y-g)
                if not k:
                    if r:
                        r[-1]=r[-1][0]+str(int(r[-1][1:])+1)
                    else:
                        r.append('D'+str(1))
                else:
                    r.append(s+str(k)),r.append('D1')
                x+=1
                y=g
            except:
                 return r[:-1]
    return r
        

print(escape([[2, 0, 0, 1, 0],
               [0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0]]))