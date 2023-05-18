import re

def licence_plate(s):
    if(not s or not re.search(r'[^0-9]',s) or re.search(r'--',s)):
        return 'not possible'
    s=re.sub(r'\s','-',re.sub(r'[0-9]+',lambda e:' '+e.group()+' ',re.sub(r'[^A-Z0-9]','-',s.upper())).strip())
    s=re.sub(r'-+','-',s)
    while s[0]=='-':
        s=s[1:]
        if(not s):
            return 'not possible'
    s=s[:8]
    while s[-1]=='-':
        s=s[:-1]
    return s if len(s)>1 and len(s)<9 and re.search(r'[^0-9]',s) else 'not possible'

print(licence_plate('~c0d3w4rs~'))
print(licence_plate('1st'))
print(licence_plate('}'))