def triple_shiftian(a,n):
    while len(a)<=n:
        a.append(4*a[len(a)-1]-5*a[len(a)-2]+3*a[len(a)-3])
    return a[n]

print(triple_shiftian([1,1,1],35))