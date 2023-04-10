def compare(a,b):
    c=str(a)
    d=str(b)
    if(c[0]==d[0] and c[1]!=d[1] or c[1]==d[0] and c[0]!=d[1] or c[1]==d[1] and c[0]!=d[0] or c[0]==d[1] and c[1]!=d[0]):
        return '50%'
    if(c[0]==d[0] and c[1]==d[1] or c[0]==d[1] and c[1]==d[0]):
        return '100%'
    else:
        return '0%'

print(compare(58,75))