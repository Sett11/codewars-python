from re import sub

def f(s):
    return s+'egg' if (s.lower() not in 'aioue' and s.isalpha()) else s

def heggeleggleggo(s):
    return sub(r'.',lambda e:f(e.group()),s)

print(heggeleggleggo('hello'))