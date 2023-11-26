from re import sub

def simplify(n):
    if n**.5==int(n**.5):
        return str(int(n**.5))
    a=[i for i in range(2,n) if n%i==0 and i**.5==int(i**.5)]
    if not a:
        return f'sqrt {n}'
    a=a[-1]
    return f'{int(a**.5)} sqrt {n//a}'

def desimplify(s):
    if s.isdigit():
        return int(s)**2
    a=list(map(int,sub(r'\D',' ',s).split()))
    if len(a)==1:
        return a[0]
    return a[0]**2*a[1]

print(simplify(945))
print(desimplify("4 sqrt 2"))