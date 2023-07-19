def adjust(b,n):
    c=min(b,n)
    while not (n<=c and c%b==0):
        c+=1
    return c

print(adjust(3,7))