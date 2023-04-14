def create_anagram(s,t,i=0):
    s=list(s);t=list(t)
    while i<len(s):
        if(t[i] in s):
            s[s.index(t[i])]='&'
        i+=1
    return len(list(filter(lambda e:e!='&',s)))

print(create_anagram("AABAA", "BBAAA"))
print(create_anagram("OVGHK", "RPGUC"))