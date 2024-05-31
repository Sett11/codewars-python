def blow_candles(s):
    c=0
    while s:
        while s.startswith('0'):
            s=s[1:]
        s,c=''.join(map(lambda x:str(max(int(x)-1,0)),s[:3]))+s[3:],c+1 if s else c
    return c

print(blow_candles('0323456'))
print(blow_candles('1321'))