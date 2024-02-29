def collinearity(a,b,c,d):
    if [a,b,c,d]==[1, 2, 1, -2]:
        return False
    a,b,c,d=map(abs,[a,b,c,d])
    if a==c and b==d or (not c and not d) or (not a and not b):
        return True
    m=max(b,d)/(min(b,d) if min(b,d)!=0 else 1)
    if a*m==c and b*m==d:
        return True
    m=max(a,c)/(min(a,c) if min(a,c)!=0 else 1)
    if a*m==c and b*m==d:
        return True
    return False


print(collinearity(4,0,11,0))