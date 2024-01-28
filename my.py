def round_and_round(n,a,b):
    r=list(range(1,n+1))
    if b>0:
        i=a-1
        while b:
            i=(i+1)%n
            b-=1
        return r[i]
    else:
        i=a-1
        while b:
            i=(i-1)
            if i<0:
                i=n-1
            b+=1
        return r[i]

print(round_and_round(5,1,3))
print(round_and_round(6,2,-5))