import re

def purify(s):
    s,i,a=list(s),0,['i','I']
    while i<len(s):
        if s[i] in a:
            s[i]='&'
            if i and s[i-1]!=' ':
                s[i-1]='&'
            if i!=len(s)-1 and s[i+1]!=' ' and s[i+1] not in a:
                s[i+1]='&'
        i+=1
    return re.sub(r'\s+',' ',''.join([i for i in s if i!='&'])).strip()

print(purify("1i2 33 i4i5 i555ii5"))
print(purify("It is a bit chilly"))
print(purify("STRING"))