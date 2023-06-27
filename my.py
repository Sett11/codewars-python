def pig_latin(s):
    return s if len(s)<4 else s[1:]+s[0]+'ay'

print(pig_latin('hello'))