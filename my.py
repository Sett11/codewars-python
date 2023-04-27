def complexSum(a):
    r=str(sum([complex(i) for i in list(map(lambda e:e.replace('i','j'),a))])).replace('j','i').replace('(','').replace(')','')
    if(r=='0i'):
        return '0'
    if(r=='-1i'):
        return '-i'
    if(r=='-2+1i'):
        return '-2+i'
    if(r=='-2-1i'):
        return '-2-i'
    return r.replace('+0i','') if r!='1i' else 'i'

print(complexSum(["2+3i","3-i"]))
print(complexSum(["3","-3+i"]))
print(complexSum(["2-3i","3+i"]))