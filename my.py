def last_digit(n1,n2):
    a,n=[n2,n1],1
    for i in a:
        n=i**(n if n<4 else n%4+4)
    return n%10

print(last_digit(2**200,2**300))