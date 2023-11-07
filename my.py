def to_seconds(s):
    try:
        a=list(map(int,s.split(':')))
        if all(i<60 and i>=0 for i in a[1:]) and all(len(i)==2 for i in s.split(':')):
            return ((a[0]*3600+a[1]*60+a[2]) or None) if s!='00:00:00' else 0
    except:
        pass

print(to_seconds('01:02:03'))