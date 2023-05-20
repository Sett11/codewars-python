bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def f(x,y,z):
    if(x<y):
        return z[x]
    a,b=divmod(x,y)
    return f(a,y,z)+z[b]

def convert(a,b,c):
    return f(sum(b.index(i)*len(b)**k for k,i in enumerate(a[::-1])),len(c),c)

print(convert('15',dec,bin))