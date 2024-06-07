def points(n):
    n*=n
    c,d=0,1
    while d<=n:
        c+=n//d
        c-=n//(d+2)
        d+=4
    return c*4+1


print(points(1000))