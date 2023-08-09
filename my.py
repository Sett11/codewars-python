def one_two_three(n):
    d=divmod(n,9)
    return [0,0] if n==0 else [int(('9'*d[0])+(str(d[1]) if d[1] else '')),int('1'*n)]
    
print(one_two_three(0))
print(one_two_three(204))
print(one_two_three(189))