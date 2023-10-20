def uglify_word(s):
    s=list(s)
    c=1
    for i in range(len(s)):
        if s[i].isalpha():
            if c:
                s[i]=s[i].upper()
            else:
                s[i]=s[i].lower()
            c=not c
        else:
            c=1
    return ''.join(s)


print(uglify_word("aaa-bbb-ccc"))