def add(n1,n2):
    n1=list(map(int,list(str(n1))))
    n2=list(map(int,list(str(n2))))
    while len(n1)<len(n2):
        n1.insert(0,0)
    while len(n2)<len(n1):
        n2.insert(0,0)
    i=len(n1)-1
    r=[]
    while i>=0:
        r.insert(0,n1[i]+n2[i])
        i-=1
    return int(''.join(list(map(str,r))))

print(add(2,11))