def some_but_not_all(s,f):
    a=0
    b=0
    for i in s:
        if(f(i)):
            a+=1
        else:
            b+=1
    return True if a and b else False

print(some_but_not_all('abcdefg&%$', str.isalpha))