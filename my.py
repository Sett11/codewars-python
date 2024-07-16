def button_sequences(a,b):
    r='R' if a[0]=='1' else 'B' if b[0]=='1' else ''
    t,q=[0] if r=='R' else [],[0] if r=='B' else []
    for i in range(1,len(a)):
        if (a[i]=='1' and b[i]=='1') or (a[i]=='1' and b[i]=='0'):
            if b[i-1]+b[i]=='11':
                continue
            x=a[t[-1]:i] if t else ''
            if x!='1'*len(x) or not x:
                r+='R'
                t.append(i)
        if b[i]=='1' and a[i]=='0':
            y=b[q[-1]:i] if q else ''
            if y!='1'*len(y) or not y:
                r+='B'
                q.append(i)
    return r


print(button_sequences('0011101110101000',
                       '1101010001011111'))