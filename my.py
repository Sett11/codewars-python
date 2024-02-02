def triangular_range(a,b):
    r,i,j=[1],1,2
    while i+j<b:
        r.append(i+j)
        i+=j
        j+=1
    return {i+1:j for i,j in enumerate(r) if j>a}

print(triangular_range(17,2220))