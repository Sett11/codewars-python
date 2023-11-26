from re import sub
from string import ascii_lowercase as a

def decode(s,c):
    r=[]

    for _ in range(26):
        if c in s:
            r.append(s)
        s=sub(r'.',lambda x: a[(a.index(x.group())+1)%26],s)
    
    return r

print(decode('ymjxvznwwjqnxhzyj','squirrel'))
print(decode('lzwespnsdmwakafxafalq','max'))