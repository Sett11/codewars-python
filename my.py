def trace(m):
    i=0
    c=0
    while i<len(m):
        j=0
        while j<len(m[i]):
            if(i==j):
                c+=m[i][j]
            j+=1
        i+=1
    return None if not len(m) or len(m)!=len(m[0]) else c

print(trace([[1,2,3], [4,5,6], [7,8,9]]))