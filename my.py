def digits(n):
    n=list(map(int,str(n)))
    a=[]
    i=0
    j=i+1
    while i<len(n):
        j=i+1
        while j<len(n):
            a.append(n[i]+n[j])
            j+=1
        i+=1
    return a

print(digits(3264128))