from re import sub

def to_cents(s):
    c=sub(r'\$\d+\.','',s)
    try:
        if len(s)!=len(c) and len(s.split('.')[1])<3 and '\n' not in s:
            return int(s[1:].replace('.',''))
    except:
        pass


print(to_cents("1"))
print(to_cents("$99.99"))