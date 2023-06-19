def seven_wonders_science(c,g,t):
    n,a,r=c**2+g**2+t**2,[c,g,t],0
    while all(a):
        r+=1
        a=[i-1 for i in a]
    return r*7+n

print(seven_wonders_science(7,2,2))