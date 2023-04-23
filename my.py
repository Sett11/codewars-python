def speed_limit(s,l):
    r=list(filter(lambda u:u>0,list(map(lambda e:s-e,l))))
    c=0
    for i in r:
        if(i<20 and i>=10):
            c+=100
        if(i>=20 and i<30):
            c+=250
        if(i>=30):
            c+=500
    return c

print(speed_limit(86, [120, 110, 100, 90, 80, 100]))