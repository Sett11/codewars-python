def is_opposite(s1,s2):
    if len(s1)!=len(s2) or not s1 and not s2:
        return False
    i=0
    while i<len(s1):
        if not s1[i].lower()==s2[i].lower() and s1[i]!=s2[i]:
            continue
        if s1[i]==s2[i]:
            return False
        i+=1
    return True

print(is_opposite("Ab","AB"))