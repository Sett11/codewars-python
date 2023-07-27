def to12hourtime(t):
    a,b=int(t[:2]),str(int(t[2:]))
    v=a>=12
    b,c=('0' if len(b)<2 else '')+b,'pm' if v else 'am' if a else 'pm'
    return f'{str(a-12 if v else a if a else 12)}:{b} {c}'

print(to12hourtime('2145'))
print(to12hourtime('1300'))
print(to12hourtime('0000'))