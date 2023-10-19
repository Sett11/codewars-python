def freed_prisoners(a):
    c=0
    if not a[0]:
        return c
    for i in range(len(a)):
        if a[i]:
            c+=1
            a=[not j for j in a]
    return c
    

print(freed_prisoners([True, True, False, False, False, True, False]))