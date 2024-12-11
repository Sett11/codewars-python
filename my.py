from string import ascii_lowercase

def decipher(a):
    s=' '+ascii_lowercase
    return ''.join(s[sum(s.index(j) for j in i)//len(i)] for i in zip(*a))

print(decipher(["u lk zxuq hfk as fouh","y l  zpuv  xe at sicd","welvayfuqbfpeaauaqcrc"]))