def find_nb(m):
    i,t=1,0
    while t<m:
        t+=i**3
        i+=1
    return i-1 if t==m else -1

print(find_nb(4183059834009))