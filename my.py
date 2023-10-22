def correctness(a,b): 
    r=[i for i in zip(a,b)]
    c=0
    for i,j in r:
        if i==j:
            c+=1
        elif i!=j and '?' in [i,j]:
            c+=.5
    return c

print(correctness(('M', '?', 'M'), ('M', 'F', '?')))