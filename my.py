def position(x,y,n):
    k,m=int(y/x),n//2
    r=[i for i in range(k-m,k+m+1)]
    while len(r)<x:
        r.append(r[-1]+1)
    while sum(r)!=y:
        t=sum(r)
        c=abs(y-t)//x
        r=list(map(lambda z:z+c if t<y else z-c,r))
    return r[n]

print(position(7,749,5))
print(position(9984, 52560768, 9699))