def r(e,o={'6':'a','1':'b','7':'d','4':'e','3':'i','2':'l','9':'m','8':'n','0':'o','5':'t'}):
    return o[e]

def hidden(n):
    a=list(str(n))
    b=map(r,a)
    return ''.join((list(b)))

print(hidden(637))