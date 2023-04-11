import re
def f(e,s='aioue'):
    return s.find(e)==-1

def count_consonants(t):
    t=re.sub(r'[^A-Za-z]+','',t)
    t=list(filter(f,t.lower()))
    a=''
    for i in range(len(t)):
        if(a.find(t[i])==-1):
            a+=t[i]
        else:
            continue
    return len(a)
   
print(count_consonants('Count my unique consonants!!'))