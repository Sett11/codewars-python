def addsup(a1,a2,a3):
    r=[]
    for i in a1:
        for j in a2:
            if(i+j in a3):
                r.append([i,j,i+j])
    return r

print(addsup([1,2,5],[3,1],[5,4,6]))