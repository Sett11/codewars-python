def numericals(s):
    d,r={},''
    for i in s:
        if i not in d:
            d[i]=1
            r+='1'
        else:
            d[i]+=1
            r+=str(d[i])
    return r

print(numericals("Hello, World! It's me, JomoPipi!"))