def unique_date(x,y,z):
    a=sorted([x,y,z])
    s,t,l=['0'+str(i) if i<10 else str(i) for i in a],[i for i in a if i<=12],set(a)
    return 'ambiguous' if (len(t)>1 and len(l)==3) or (len([i for i in a if i<=31])==3 and 0 not in a and len(l)==3) or (len(l)==2 and len([i for i in a if i<=31])==3 and 0 not in a and len([i for i in a if i<=12])>=2) else f'{s[-1]}/{s[0]}/{s[1]}' if (len([i for i in a if i<=12]) and len([i for i in a if i<=31])) else 'invalid'

print(unique_date(2, 2, 12))