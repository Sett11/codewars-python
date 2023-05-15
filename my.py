def f(x):
    i=0
    a=[]
    while i<len(x[0]):
        j=0
        b=[]
        while j<len(x):
            b.append(x[j][i])
            j+=1
        a.append(sorted(b))
        i+=1
    return a

def order(m):
    return f(f([sorted(i) for i in m]))

print(order([[7,  1,  4, 37, 28], 
           [3,  2,  8, 12, -8],
           [6, -1, -6,  7, 55]] ))