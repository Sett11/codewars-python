def esrever(s):
    if(len(s)==0):return ''
    c=s[len(s)-1];s=s[:-1]
    return ' '.join(list(map(lambda e: ''.join(list(e)[::-1]), s.split()))[::-1])+c

print(esrever('hello world.'))