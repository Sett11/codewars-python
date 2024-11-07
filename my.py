def page_digits(n):
    c,l,s=0,1,1
    while s<=n:
        e=min(n,s*10-1)
        x=e-s+1
        c+=x*l
        l+=1
        s*=10
    return c


print(page_digits(100))
print(page_digits(4234))
print(page_digits(6572))