def martingale(b,a):
    c=100
    for i in a:
        if(i):
            b+=c
            c=100
        else:
            b-=c
            c*=2
    return b

print(martingale(-500, [1, 1, 0, 1, 0, 1, 0]))