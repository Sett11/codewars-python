def crosstable(a,r):
    n,q,u=len(a),{},set()
    m=sb=pts=c=0
    w={a[i]:{'score':sum([j for j in r[i] if j]),'wins':[a[j] for j in range(len(a)) if r[i][j]==1],'draw':[a[j] for j in range(n) if r[i][j]==.5],'SB':0} for i in range(len(a))}
    for i in w:
        for j in w[i]['wins']:
            w[i]['SB']+=w[j]['score']
        for j in w[i]['draw']:
            w[i]['SB']+=w[j]['score']/2
        w[i]['SB']=float(w[i]['SB'])
        w[i]['score']=float(w[i]['score'])
    w=sorted([(i[0],(i[1]['score'],i[1]['SB'])) for i in w.items()],key=lambda x:(-x[1][0],-x[1][1],x[0].split()[1]))
    for i in range(n):
        w[i]=[str(i+1),w[i][0],w[i][1][0],w[i][1][1]]
        q[w[i][1]]=i
        m,c=max(m,len(w[i][1])),max(c,len(w[i][0]))
    for i in range(n):
        y,z=str(w[i][2]),(str(w[i][3])+'0') if len(str(w[i][3]).split('.')[1])<2 else str(w[i][3])
        t,x,pts,sb=r[a.index(w[i][1])],(y,z),max(pts,len(y)),max(sb,len(z))
        s=' '.join(('=' if k[1]==.5 else '1' if k[1]==1 else '0' if k[1]==0 else ' ').rjust(len(str(n)),' ') for k in sorted([(a[j],t[j]) for j in range(n)],key=lambda x:q[x[0]]))
        w[i]=[(w[i][0] if x not in u else ' '),w[i][1],s,*x]
        u.add(x)
    for i in range(n):
        w[i]='  '.join([w[i][0].rjust(c,' '),w[i][1].ljust(m,' '),w[i][2],w[i][3].rjust(pts),w[i][4].rjust(sb)])
    st='  '.join(['#'.rjust(len(str(n)),' '),'Player'.ljust(m),' '.join([str(i).rjust(len(str(n))) for i in range(1,n+1)]),'Pts'.center(pts),'BS'.center(sb)[::-1]])
    w.insert(0,st.rstrip()),w.insert(1,'='*len(st))
    return '\n'.join(w)

d, _ = 0.5, None
print(crosstable([
            'K. Kel', 'A. Vau', 'Z. Aya', 'J. Coc', 'M. Hue', 'A. Sim', 'C. Yan', 'J. Wal',
            'M. Hor', 'L. Ell', 'H. Mic', 'P. Bla', 'L. Lan', 'M. Rid', 'M. Bec', 'J. Gat'], [
            [_, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, _, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, _, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, _, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, _, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, _, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, _, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 1, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, _, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, _, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _]]))