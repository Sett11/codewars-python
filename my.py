def sentencify(a):
    s=' '.join(a)+'.'
    return s[0].upper()+s[1:]


print(sentencify(["i", "am", "an", "AI"]))