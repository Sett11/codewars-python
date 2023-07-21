import re
def fn_shorthand(s):
    c,i=list(re.sub(r' +',' ',s)),0
    while i<len(c):
        if c[i]=='>':
            c[i]='('
            c+=')'
        i+=1
    return re.sub(r' ',',',''.join(c)).replace(',(','(').replace('(,','(')

print(fn_shorthand("max > list > 9**5 7**9"))
print(fn_shorthand("list > map > upper set > a b"))
print(fn_shorthand("fn>fn>fn>fn>fn>fn>fn>"))
print(fn_shorthand("print > 1 2 3"))