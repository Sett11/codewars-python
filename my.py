def encoder(s):
    d,r,c,k={s[0]:'1'},'0'+s[0],2,''
    for i in s[1:]:
        k+=i
        if k not in d:
            d[k]=str(c)
            if len(k)==1:
                r+='0'+k
            else:
                r+=d[k[0:-1]]+k[-1]
            c+=1
            k=''
    return r+d.get(k,'')

def decoder(s):
    d,r,c,k={'0':'','1':s[1]},s[1],'',2
    for i in s[2:]:
        if i.isdigit():
            c+=i
        else:
            d[str(k)]=d[c]+i
            r+=d[c]+i
            c=''
            k+=1
    return r+d.get(c,'')

print(encoder('ABAABABAABABAA'))
print(decoder('0A0B1A2A4A4B3'))