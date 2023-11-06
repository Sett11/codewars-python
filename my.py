def xmastree(n):
    r=[]
    i=1
    while len(r)<n:
        t='_'*(n-i)+'#'*i+'_'*(n-i)
        while len(t)<n*2-1:
            t='_'+t+'_'
        r.append(t)
        i+=2
    r.extend([r[0],r[0]])
    return r

print(xmastree(16))