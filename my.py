def decipher(s,i=1,c=''):
    while i<len(s):
        a=int(s[slice(i)])
        if(a>=96 and a<=122):
            c+=chr(a)
            s=s[slice(i,len(s))]
            i=1
        i+=1
    c+=chr(int(s))
    return c

print(decipher('10197115121'))