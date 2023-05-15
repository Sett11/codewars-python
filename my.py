import re as r
def frogify(s):
   print(s)
   s=([' '.join(i.strip().split(' ')[::-1]) for i in r.sub(r'\.|\!|\?',lambda e:'&'+e.group()+'&',s).split('&') if i])
   return ' '.join([r.sub(r'[^ a-z]','',i) if i!='.' and i!='!' and i!='?' else i for i in s]).strip().replace('  ',' ').replace(' .','.').replace(' ?','?').replace(' !','!').replace('  ',' ').replace(' .','.')

print(frogify('multisentence is good. is not it?'))
print(frogify("look, a fly!"))
print(frogify('oven ducks seemly yoke flower destroy. (.'))