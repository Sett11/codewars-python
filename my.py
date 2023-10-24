def evil_code_medal(t,g,s,b):
    a=[i for i in [g,s,b] if i>t]
    if a:
        a=a[0]
        return 'Gold' if a==g else 'Silver' if a==s else 'Bronze'
    return 'None'

print(evil_code_medal("00:30:00","00:15:00","00:45:00","01:15:00"))