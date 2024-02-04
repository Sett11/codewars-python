def d(a):
    n,m,r,q,v=len(a),len(a[0]),[],[],2
    while v:
        w=v==2
        for i in range(n-(0 if w else 1)):
            k,j,t=i,0,[]
            while k>=0 and j<m:
                t.append(a[k][j])
                k-=1
                j+=1
            r.append(t) if w else q.insert(0,t)
        v-=1
        a=[p[::-1] for p in a][::-1]
    return [i for i in r+q if len(i)>3]

def f(a,n,c):
    for i in range(len(a)-1,-1,-1):
        if a[n][i]==0:
            a[n][i]=c
            return a
        
def check(a):
    return [i for i in a if i.count('Yellow')>3 or i.count('Red')>3]


def who_is_winner(a):
    r,s=[[0]*7 for _ in range(7)],'ABCDEFG'
    for i in range(len(a)):
        b,c=a[i].split('_')
        f(r,s.index(b),c)
        v=check(d(r)+d([p[::-1] for p in r])+r+[list(i) for i in zip(*r)])
        if v:
            for k in v:
                for j in range(len(k)):
                    if k[j]=='Yellow' and k[j:j+4]==['Yellow']*4:
                        return 'Yellow'
                    if k[j]=='Red' and k[j:j+4]==['Red']*4:
                        return 'Red'
    return 'Draw'

print(who_is_winner([
"F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", 
"B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", 
"F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", 
"A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", 
"B_Yellow", "B_Red"
]))