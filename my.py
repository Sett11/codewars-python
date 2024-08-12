from re import sub

def phone_number(a):
    def f(a):
        d,z={},{}
        for i in a:
            if i:
                d[i[0]]=d.get(i[0],[])+[i[1:]]
        for i in d:
            t=f(d[i])
            if len(t)==1 and '' not in d[i]:
                for j in t:
                    i,t=i+j,t[j]
            z[i]=t
        return z
    return len(sub(r'[^\d]','',str(f(a))))


print(phone_number([
            '0123456789',
            '0123987654',
            '0123987456',
            '2365498756',
            '2365498765']))