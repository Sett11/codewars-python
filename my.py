def f(e):
    a=ord(e)
    if(a>64 and a<91):return chr((26-(a-65))+64)
    if(a>96 and ord(e)<123):return chr((26-(a-96))+97)
    return e
def decode(s):
    return 'Input is not a string' if not isinstance(s,str) else ''.join(list(map(f,list(s))))

print(decode("Ovg'h hdrn rm gsv ulfmgzrm!"))