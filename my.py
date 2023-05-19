import math as m
def decipher_message(s):
    n=int(m.sqrt(len(s)))
    return ''.join([''.join(list(i)) for i in list(zip(*[list(s[i:i+n]) for i in range(0,len(s),n or 1)]))])

print(decipher_message('ArNran u rstm5twob  e ePb'))