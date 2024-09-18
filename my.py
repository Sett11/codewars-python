def d(a):
    n,m,r=len(a),len(a[0]),[]
    for i in range(n+m-1):
        k,j,t=0 if i<m else i-m+1,i if i<m else m-1,[]
        while k<n and j>=0:
            t.append(a[k][j])
            k+=1
            j-=1
        r.append(''.join(t))
    return r

def how_many_bees(a):
    return sum(i.count('bee')+i.count('eeb') for i in [''.join(i) for i in a]+[''.join(i) for i in zip(*a)]+d(a)+d(a[::-1])) if a else 0

print(how_many_bees([
'...ee.beb',
'e..e.beb.',
'..beeb..e']),sep='\n')