def decode(s):
    a='abcdefghijklmnopqrstuvwxyz'
    return ''.join([a[-a.index(i)-1] if i!=' ' else i for i in s])

print(decode('abc jko'))