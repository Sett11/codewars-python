def tops(s):
    i,j=1,2
    c=''

    while i<len(s):
        c+=s[i]
        i+=j*2+1
        j+=2

    return c[::-1]

print(tops('abcdefghijklmnopqrstuvwxyz12345'))