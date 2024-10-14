def triangle(s):
    d={'BB': "B", 'BG': "R", 'BR': "G", 'GB': "R", 'GG': "G", 'GR': "B", 'RB': "G", 'RG': "B", 'RR': "R"}
    while len(s)>1:
        n,r,c=len(s),'',1
        while n%(c*3)==1:
            c*=3
        for i in range(0,n-1,c):
            r+=d[s[i]+s[i+c]]
        s=r
    return s


print(triangle('RBRGBRBGGRRRBGBBBGG'*100))
print(triangle('RRBGBBBGGRBRGBRBGGR'*100))