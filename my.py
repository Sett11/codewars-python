from itertools import groupby

def replace(s):
    a,u=[(i,len(list(j))) for i,j in groupby(s)],set()
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i][0]!=a[j][0] and a[i][1]==a[j][1] and j not in u and i not in u:
                a[i]=a[j]=(' ',a[i][1])
                u.update([i,j])
                break
    return ''.join(i[0]*i[1] for i in a)

print(replace('!?!!??!!!?'))
print(replace('!????!!!?'))