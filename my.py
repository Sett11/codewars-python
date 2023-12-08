from copy import deepcopy

def f(a):
    return list([list(j) for j in zip(*[i for i in a])])[::-1]

def rotate_like_a_vortex(matrix):
    a=deepcopy(matrix)
    n,k,i,x=len(a),1,0,['&']*len(a)
    
    while n>i:
        v=k
        while v:
            r=f([j[i:n] for j in a][i:n])
            while v>1:
                r=f(r)
                v-=1
            v-=1
        while len(r)!=len(a):
            for h in range(len(r)):
                r[h]=['&']+r[h]+['&']
            r.insert(0,x)
            r.append(x)
        for c in range(len(r)):
            n-=1
            if r[c][i]!='&':a[c][i]=r[c][i]
            if r[c][n]!='&':a[c][n]=r[c][n]
            if r[i][c]!='&':a[i][c]=r[i][c]
            if r[n][c]!='&':a[n][c]=r[n][c]
            n+=1
        n-=1
        i+=1
        k+=1

    return a
    
    


print(rotate_like_a_vortex([
                   [ 5, 3, 6, 1 ],
                   [ 5, 8, 7, 4 ],
                   [ 1, 2, 4, 3 ],
                   [ 3, 1, 2, 2 ] ]))