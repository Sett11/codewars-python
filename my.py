def fifo(n,a):
    r,j=[-1]*n,0

    for i in a:
        if len(r)==n:
            if i not in r:
                r[j%n]=i
                j+=1
        else:
            r[j]=i

    return r

print(fifo(3, [1, 2, 3, 4, 2, 5]))