def balance_statement(s):
    a,d,bad=[i.strip().split() for i in s.split(',')],{'Buy':0,'Sell':0,'Badly formed':0},[]
    if a and a[0]:
        for i in a:
            if len(i)!=4 or ' ' in i[0] or not i[1].isdigit() or '.' not in i[2] or not i[2].replace('.','').isdigit() or i[3] not in 'BS':
                d['Badly formed']+=1
                bad.append(i)
                continue
            n=round(int(i[1])*float(i[2]))
            if i[-1]=='B':
                d['Buy']+=n
            if i[-1]=='S':
                d['Sell']+=n
    if not d['Badly formed']:
        del d['Badly formed']
    return f"Buy: {d['Buy']} Sell: {d['Sell']}{('; Badly formed '+str(d['Badly formed'])+': '+' ;'.join([' '.join(i) for i in bad])+' ;') if 'Badly formed' in d else ''}"

print(balance_statement("ZNGA 1300 2.66, CLH15.NYM 50 56.32 S, OWW 1000 11.623 S, OGG 20 580.1 S"))
print(balance_statement("GOOG 300 542.93 B, CLH15.NYM 50 56.32 S, CSCO 250 29.46 B, OGG 20 580.1 B"))
print(balance_statement("GOOG 90 160.45 B, JPMC 67 12.8 S, MYSPACE 24.0 210 B, CITI 50 450 B, CSCO 100 55.5 S"))