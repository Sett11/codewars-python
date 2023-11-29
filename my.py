def substring(s):
    o={0:''}
    m=0
    s+='0'

    for i in range(len(s)):
        c=set()
        c.add(s[i])
        for j in range(i+1,len(s)):
            c.add(s[j])
            if len(c)>2 or '0' in c:
                t=s[i:j]
                n=len(t)
                m=max(m,n)
                if n not in o:
                    o[n]=t
                break
    
    return o[m]

print(substring('cefageaacceaccacca'))
print(substring('bbacddddcdd'))
print(substring('aaaaa'))