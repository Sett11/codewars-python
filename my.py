def london_city_hacker(a): 
    c=i=0
    d=[2.40,1.50]
    n=len(a)
    while i<n:
        t=type(a[i])==int
        if i==n-1:
            c+=d[t]
            break
        elif type(a[i])==type(a[i+1]) and t:
            c+=d[t]
            i+=2
        else:
            c+=d[t]
            i+=1
    r=str(round(c,2)).split('.')
    if len(r)==2:
        r[1]=r[1].ljust(2,'0')
    else:
        r.append('00')
    r='.'.join(r)
    return '£'+r

print(london_city_hacker([12, 'Central', 'Circle', 21]))