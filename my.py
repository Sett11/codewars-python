def is_keith_number(n):
    if n<10:
        return False
    a,i=list(map(int,str(n))),1
    while True:
        s=sum(a)
        if s==n:
            return i
        if i>100:
            return False
        a=a[1:]
        a.append(s)
        i+=1

print(is_keith_number(196))