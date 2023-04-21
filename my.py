def a1_thick_and_hearty(a1,a2):
    l1=len(a1)
    l2=len(a2)
    a1=list(filter(lambda e:e in a2,a1))
    a2=list(filter(lambda e:e in a1,a2))
    r=[]
    i=0
    j=i+1
    while i<len(a1):
        j=i+1
        while j<len(a1):
            if(a1[i]+a1[j]==l1 or a1[i]-a1[j]==l1 or a1[i]+a1[j]==l2 or a1[i]-a1[j]==l2 or a1[j]-a1[i]==l1 or a1[j]-a1[i]==l2):
                r.append(a1[i])
                r.append(a1[j])
            j+=1
        i+=1
    return set(r)

print(a1_thick_and_hearty([1, 2, 3, 5, 10, 15],[1, 2, 3, 4, 5, 6, 10, 12, 15, 16]))