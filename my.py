def scf(a,i=2):
    if(len(a)==0):return 1
    m=max(a);n=max(a)
    while i<max(a)/2+1:
        if(len(list(filter(lambda e: e%i==0,a)))==len(a)):
            m=min(m,i)
        i+=1
    return m if m!=n else 1

print(scf([133, 147, 427, 266]))
print(scf([3,5,7]))