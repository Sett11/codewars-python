def atomic_number(e):
    r=[]
    i=1
    while e>0:
        r.append(2*i**2)
        e-=2*i**2
        i+=1
    r[len(r)-1]+=e
    return r

print(atomic_number(61))