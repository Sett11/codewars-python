def AlphaNum_NumAlpha(s):
    r=[]
    i=0
    j=0
    while i<len(s):
        if(s[i].isalpha()):
            r.append(s[i])
        if(s[i].isdigit()):
            j=i
            while j<len(s):
                if(s[j].isalpha()):
                    r.append(s[slice(i,j)])
                    i=j-1
                    break
                if(j==len(s)-1):
                    r.append(s[slice(i,j+1)])
                    i=j
                    break
                j+=1
        i+=1
    return ''.join(map(str,[ord(i)-96 if i.isalpha() else chr(int(i)+96) for i in r]))

print(AlphaNum_NumAlpha('5a8p17'))