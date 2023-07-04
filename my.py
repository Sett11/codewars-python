def check_grid(l,p,s):
    b,a=p
    c,aa,bb,r,t=[list(j) for i,j in enumerate(zip(*l)) if i==b][0],a,b,[],[]
    while aa<s and bb<s:
        r.append(l[aa][bb])
        aa+=1
        bb+=1
    aa,bb=a-1,b-1
    while aa>=0 and bb>=0:
        r.append(l[aa][bb])
        aa-=1
        bb-=1
    aa,bb=a,b
    while aa<s and bb>=0:
        t.append(l[aa][bb])
        aa+=1
        bb-=1
    aa,bb=a-1,b+1
    while aa>=0 and bb<s:
        t.append(l[aa][bb])
        aa-=1
        bb+=1
    return [sorted(i) for i in [l[a],c,r,t]]


print(check_grid([
[ 1,  2,  3,  4,  5],
 [ 6,  7,  8,  9,  0],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20],
 [21, 22, 23, 24, 25]],[2,3],5))