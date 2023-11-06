def counting_valleys(s): 
    a=[0 if i=='F' else 1 if i=='U' else -1 for i in s]
    r=c=0
    v=False
    for i in a:
        r+=i
        if r<0:
            v=True
        elif r>=0 and v:
            v=False
            c+=1
    return c


print(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'))