def set_clock(s,t):
    a,b=map(int,s.split(':'))
    for i in t:
        if i=='H':
            a+=1
        else:
            b+=1
    return f"{a-24 if a>24 else a}:{('0' if b%60<10 else '')+str(b%60)}"

print(set_clock("23:59", ['H', 'H']))