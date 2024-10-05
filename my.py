from decimal import Decimal as d

def cuckoo_clock(t,n):
    y=float(t.replace(':','.'))
    if y%1==0:
        n-=y
    t,c=d(t.replace(':','.')),d('0.01')
    while n>0:
        s=str(t).split('.')
        if s[1] in ['15','30','45']:
            n-=1
        if s[1]=='60':
            x=(int(s[0])%12)+1
            n-=x
            t=d(x)
        if n>0:
            t+=c
    r=str(t).rjust(2,'0').replace('.',':')
    return r.rjust(5,'0') if ':' in r else r+':00'

print(cuckoo_clock('03:38',19))
print(cuckoo_clock("09:53",50))
print(cuckoo_clock("10:00",10))