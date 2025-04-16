def split_numbers(n):
    x=bin(n)[2:][::-1]
    a,b=list('0'*len(x)),list('0'*len(x))
    n=1
    for i in range(len(x)):
        if x[i]=='1' and n&1:
            a[i]='1'
            n += 1
        elif x[i]=='1' and not n&1:
            b[i]='1'
            n += 1
    return int(''.join(a[::-1]),2),int(''.join(b[::-1]),2)

print(split_numbers(13))
