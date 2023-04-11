def encode(s):
    l='abcdefghijklmnopqrstuvwxyz'
    s=s.lower()
    a=''
    i=0
    while i<len(s):
        if(l.find(s[i])!=-1):
            if(l.find(s[i])%2)==0:
                a+='0'
            else:
                a+='1'
        else:
            a+=s[i]
        i+=1
    return a

print(encode("Hello World!"))