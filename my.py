def basereduct(n):
    i=0
    while i<150:
        s=sorted(str(n))
        if '9' not in s:
            n=int(str(n),int(s[-1])+1)
        else:
            n=int(str(n),11)
        i+=1
        if len(str(n))==1:
            return n
    return -1

print(basereduct(5312))