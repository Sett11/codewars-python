def string_hash(s):
    q=[ord(i) for i in s]
    a=sum(q)
    b=sum([q[i+1]-q[i] for i in range(len(q)-1)])
    c=(a|b)&((~a)<<2)
    return c^(32*(s.count(' ')+1))

print(string_hash(" Yo - What's Good?! "))