def valid_parentheses(s):
    i=0
    c=0
    while i<len(s):
        if(c==-1):
            return 1==2
        if(s[i])=='(':
            c+=1
        if(s[i]==')'):
            c-=1
        i+=1
    return c==0

print(valid_parentheses(")()"))