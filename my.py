import re

def is_isogram(s):
    if(not isinstance(s,str) or s==''):
        return False
    s=re.sub(r'[^a-z]','',s.lower())
    i=0
    o={}
    while i<len(s):
        if(s[i] in o):o[s[i]]+=1
        else:o[s[i]]=1
        i+=1
    return len(set(o.values()))==1