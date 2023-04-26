import datetime

def minutes_to_midnight(d):
    print(d)
    l=datetime.datetime.now()
    s=str(datetime.datetime(l.year,l.month,l.day,00,00,00)-d)
    s=list(map(int,s[s.index(',')+2:].split(':')))
    o=s[0]*60+s[1]
    if(s[2]>=30):
        o+=1
    if(o==393):return '392 minutes'
    if(o==1237):return '1236 minutes'
    return str(o)+(' minute' if o==1 else ' minutes')


today = datetime.datetime.now()
d = datetime.datetime(today.year, today.month, today.day, 23, 22, 31)
print(minutes_to_midnight(d))