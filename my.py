def noonerize(n):
    try:
        a,b=list(str(n[0])),list(str(n[1]))
        a[0],b[0]=b[0],a[0]
        a,b=int(''.join(a)),int(''.join(b))
        return max(a,b)-min(a,b)
    except:
        return 'invalid array'
    

print(noonerize([12,34]))