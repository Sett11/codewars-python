def multiplication_table(s):
    a=[]
    b=[]
    i=1
    j=1
    while i<=s:
        while j<=s:
            b.append(i*j)
            j+=1
        a.append(b)
        j=1
        i+=1
        b=[]
    return a

print(multiplication_table(3))