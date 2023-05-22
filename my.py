import re
def get_char_count(s):
    s=list(re.sub(r'[^a-z0-9]','',s.lower()))
    i=0
    l=[]
    while len(s):
        i%=len(s)
        l.append([s.count(s[i]),s[i]])
        s=[j for j in s if j!=s[i]]
        i+=1
    i=0
    while i<len(l):
        j=i+1
        while j<len(l):
            if(l[i][0]==l[j][0]):
                l[i].extend(l[j][1])
                l.pop(j)
                j-=1
            j+=1
        i+=1
    l=sorted(l,reverse=True)
    return dict([[i[0],sorted(i[1:])] for i in l])

print(get_char_count('Mississippi'))