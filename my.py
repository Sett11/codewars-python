def increment(n,k,c):
    i,l,x=0,len(str(n)),c
    while i<k:
        s=str(n)
        i+=1
        g=c%l
        n+=10**(l-g-1)
        z=str(n)
        if len(z)>len(s):
            l=len(z)
            c=g+1
        c+=x
    return n
        

print(increment(50,10,0))
print(increment(1,10,1))
print(increment(1,10,10))
print(increment(14123,15,6))
print(increment(9999,9,9))