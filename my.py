def pyramid_height(n):
    c,i=0,1
    while n>=i**2:
        n-=i**2
        i+=1
        c+=1
    return c

print(pyramid_height(6201))