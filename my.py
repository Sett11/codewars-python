def convert(s):
    s=s.lower()
    a,d,j='1023456789',{},0
    for i in s:
        if i not in d:
            d[i]=a[j%9]
            j+=1
    return int(''.join(d[i] for i in s)) if d else 0

print(convert('CodeWars'))
print(convert('KATA'))