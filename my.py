def to_bytes(n):
    n=bin(n)[slice(2,100)];a=[]
    while len(n)%8!=0:
        n='0'+n
    i=0
    while i<len(n):
        a.append(n[slice(i,i+8)])
        i+=8
    return a

print(to_bytes(0xffff))