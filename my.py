def left(s,i=1):
    return s[:s.index(i)] if type(i)==str else s[:i] if i>0 else s[:-abs(i)] if i else ''

def right(s,i=1):
    return s.split(i)[::-1][0] if type(i)==str else s[-i:] if i else ''

print(left('Hello (not so) cruel World!','o'))
print(right("Don't Repeat Yourself","Repeat"))