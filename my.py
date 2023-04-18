def bracket_pairs(s):
    a=[];i=0;j=i+1;c=0
    while i<len(s):
        if(s[i]=='('):
            c+=1
            j=i+1
            while j<len(s):
                if(s[j]=='('):
                    c+=1
                if(s[j]==')'):
                    c-=1
                if(c==0):
                    a.append([i,j])
                    break
                j+=1
        i+=1
    return False if s.count('(')!=s.count(')') or c!=0 else dict(a)

print(bracket_pairs('))))))))(x)()x()))'))