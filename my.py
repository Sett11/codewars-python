def encode(s):
    c,i='',0
    while i<len(s)//2+(1 if len(s)&1 else 0):
        c+=s[i]+s[len(s)-i-1]
        i+=1
    return c[:-1] if len(s)&1 else c
    
def decode(s):
    q,w,i='','',0
    while i<len(s):
        if not i&1:
            q+=s[i]
        else:
            w+=s[i]
        i+=1
    return q+w[::-1]

print(encode('codewars'))
print(encode('white'))
print(encode("You have chosen to translate this kata."))

print(decode('csordaew'))
print(decode('wehti'))
print(decode('Y.oaut ahka vsei hcth oesteanl stnoa rt'))