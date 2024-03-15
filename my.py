def calc_poly(a,x):
    n,r=len(a),''
    for i in range(n):
        r=r+f" {'+' if a[i]>0 else '-'} {abs(a[i])}*x^{n-i-1}" if a[i] else r
    r=r.replace('^1','')[3:].replace('*x^0',' with x')
    r='For '+r+f" = {x} the value is {eval(('-' if a[0]<0 else '')+r.replace('with x','').replace('^','**'))}"
    if 'with x' not in r:
        r=r.replace('=','with x =')
    if a[0]<0:
        r=r.replace('For ','For -')
    return r.replace(' 1*',' ').replace('-1*x','-x')

print(calc_poly([2, 0, 5, -6, 4, 0], 2))
print(calc_poly([-5, 40, -28],-18))