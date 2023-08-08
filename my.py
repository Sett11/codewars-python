def replace_nth(t,n,o,v):
    if n<=0 or n>t.count(o):
        return t
    t,i,c=list(t),0,0
    while i<len(t):
        if t[i]==o:
            c+=1
        if t[i]==o and c==n:
            t[i],c=v,0
        i+=1
    return ''.join(t)

print(replace_nth("Vader said: No, I am your father!", 2, 'a', 'o'))