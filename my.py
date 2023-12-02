def smallest_integer(a,i=0,j=0):
    r=[]
    for i in a.copy():
        r.extend(i)
    r=list(set(r))
    while j<=max(r)+1:
        if(not j in r):
            return j
        j+=1