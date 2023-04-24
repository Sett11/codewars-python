def alphabetic(s):
    r=list(map(ord,list(s)))
    return r==sorted(r)

print(alphabetic('kata'))
print(alphabetic('ant'))