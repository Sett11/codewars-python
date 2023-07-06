def err_bob(s):
    s=s.split(' ')
    for i in range(len(s)):
        if not s[i]:
            continue
        j=len(s[i])-1
        while not s[i][j].isalpha():
            j-=1
        t=s[i][j]
        if t not in 'AIOUEaioue':
            if t.isupper():
                s[i]=s[i][:j+1]+'ERR'+s[i][j+1:]
            else:
                s[i]=s[i][:j+1]+'err'+s[i][j+1:]
    return ' '.join(s)

print(err_bob('THIS, is crazy!'))
print(err_bob("Punctuation? is, important!  double space also"))