def layers(n):
    c=l=1
    while c**2<n:
        c+=2
        l+=1
    return l

print(layers(50))