def mountains_of_hoiyama(n):
    i,a,k,c=n,[],1,0
    while i>0:
        t,j=[],k
        while len(t)<=i//2:
            t.append(j)
            j+=1
        i-=2
        k+=2
        c+=sum(t+t[::-1][1:])
    return c

print(mountains_of_hoiyama(7))