def count_duplicates(a,b,c):
    i=0;r=[];x=0
    while i<len(a):
        r.append(a[i]+str(b[i])+str(c[i]))
        i+=1
    i=0;j=i+1
    while i<len(r):
        while j<len(r):
            if(r[i]==r[j]):
                x+=1
                break
            j+=1
        i+=1;j=i+1
    return x
    

print(count_duplicates( ['Jack','Ben','Jack','Ben','Jack','Jack']
        ,[25,25,34,25,25,34]
        ,[180,180,200,180,180,200]))