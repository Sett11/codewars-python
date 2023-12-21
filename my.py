def remove(s,d):
    for i in d:
        s=s.replace(i,'',d[i])
    return s

print(remove('this is a string',{'t':1, 'i':2}))