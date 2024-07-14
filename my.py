def increasing_number(x,n):
    c=1
    while n:
        while x%c!=0:
            x+=1
        c+=1
        n-=1
    return x

print(increasing_number(4,5))